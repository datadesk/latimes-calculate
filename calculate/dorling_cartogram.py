import math
from django.contrib.gis.geos import Point


class dorling_cartogram(object):
    """
    Takes a GeoDjango queryset and creates a cartogram of circles based on 
    the Dorling algorithm.
    
    User must provide a queryset and strings pointing to the data attribute
    and the polygon attribute.
    
    The returned queryset will contain a new attribute, 'circle', that contains
    a polygon object ready to be rendered.
    
    Example usage:
        
        >> import calculate
        >> from models import Geography
        >> queryset = Geography.objects.all()
        >> cartogram = calculate.dorling_cartogram(queryset, 'population', 'polygon')
        # Now run the expensive task that creates the cartogram
        >> cartogram.make()
        # Now each shape in the queryset has a new 'circle' attr that is cartogram.
        >> [i.circle for i in cartogram.results]
    
    Based on code published by Zachary Forest Johnson
    
        http://indiemaps.com/blog/2008/01/dorlingpy/
    
    """
    def __init__(self, queryset, data_attr, polygon_attr, iterations=500,
        friction=0.25, ratio=0.4, scale=None):
        self.queryset = queryset
        [setattr(obj, 'i', i) for i, obj in enumerate(self.queryset)]
        self.data_attr = data_attr
        self.polygon_attr = polygon_attr
        self.iterations = iterations
        self.n = len(queryset)
        self.friction = friction
        self.ratio = ratio
        self.widest_radius = 0.0
        self.x_vectors = dict((i, 0.0) for i in range(self.n))
        self.y_vectors = dict((i, 0.0) for i in range(self.n))
        self.x_values = dict((i, getattr(obj, self.polygon_attr).centroid.x) for i, obj in enumerate(self.queryset))
        self.y_values = dict((i, getattr(obj, self.polygon_attr).centroid.y) for i, obj in enumerate(self.queryset))
        self.data_values = dict((i, getattr(obj, self.data_attr)) for i, obj in enumerate(self.queryset))
        self.perimeter_values = dict((i, 0.0) for i in range(self.n))
        self.border_values = dict((i, {}) for i in range(self.n))
        self.total_distance = 0.0
        self.total_radius = 0.0
        self.radius_values = {}
        self.tree = {}
        self.end_pointer = 1
        self.scale = scale
        self.neigbors_within_distance = 0
        self.neighbor_counts = {}
        # Mysterious name from code I'm rewriting
        self.mylist = {}
    
    def make(self):
    
        #
        # Determine the neighbors of each object and our global scale
        #
        
        for obj in self.queryset:
            this_polygon = getattr(obj, self.polygon_attr)
            this_data = getattr(obj, self.data_attr)
            obj.neighbor_list = []
            for other in [x for x in self.queryset if x.i != obj.i]:
                other_polygon = getattr(other, self.polygon_attr)
                other_data = getattr(other, self.data_attr)
                shared_border = this_polygon.intersection(other_polygon).length
                if shared_border:
                    obj.neighbor_list.append(other)
                    self.border_values[obj.i][other.i] = shared_border
                    self.perimeter_values[obj.i] += shared_border
                    xd = (this_polygon.centroid.x - other_polygon.centroid.x)
                    yd = (this_polygon.centroid.y - other_polygon.centroid.y)
                    self.total_distance += math.sqrt(xd*xd+yd*yd)
                    self.total_radius += math.sqrt(this_data/math.pi) + math.sqrt(other_data/math.pi)
            self.neighbor_counts[obj.i] = len(obj.neighbor_list)
        # Set the scale
        if not self.scale:
            self.scale = self.total_distance / self.total_radius
        
        #
        # Calculate the radii we'll start with
        #
        
        for obj in self.queryset:
            this_radius = self.scale * math.sqrt(getattr(obj, self.data_attr)/math.pi)
            self.radius_values[obj.i] = this_radius
            obj.radius = this_radius
            if this_radius > self.widest_radius:
                self.widest_radius = this_radius
            obj.circle = getattr(obj, self.polygon_attr).centroid.buffer(this_radius)
        
        #
        # Make the moves
        #
        
        for iteration in range(self.iterations):
            self.end_pointer = 1
            self.tree = dict((i, {'id': 0}) for i in range(self.n))
            [self.add_point(1, 1, obj) for obj in self.queryset]

            for obj in self.queryset:
                self.neighbors_within_distance = 0
                distance = self.widest_radius + obj.radius
                self.get_point(1, 1, obj, distance)
                xrepel = yrepel = 0.0
                xattract = yattract = 0.0
                closest = self.widest_radius
            
                # Work out repelling force of overlapping neighbours
                if self.neighbors_within_distance > 0:
                    for i in range(self.neighbors_within_distance):
                        other = self.mylist[i]
                        if other != obj.i:
                            xd = self.x_values[other]-self.x_values[obj.i]
                            yd = self.y_values[other]-self.y_values[obj.i]
                            dist = math.sqrt(xd * xd + yd * yd)
                            if dist < closest:
                                closest = dist
                            overlap = obj.radius + self.radius_values[other] - dist
                            if overlap > 0.0:
                                if dist > 1.0:
                                    xrepel = xrepel - overlap*(self.x_values[other]-self.x_values[obj.i])/dist
                                    yrepel = yrepel - overlap*(self.y_values[other]-self.y_values[obj.i])/dist
                
                # Work out forces of attraction between neighbours
                this_polygon = getattr(obj, self.polygon_attr)
                for other in obj.neighbor_list:
                    if other.i != 0:
                        other_polygon = getattr(other, self.polygon_attr)
                        xd = (this_polygon.centroid.x-other_polygon.centroid.x)
                        yd = (this_polygon.centroid.y-other_polygon.centroid.y)
                        dist = math.sqrt(xd * xd + yd * yd)
                        overlap = dist - obj.radius - other.radius
                        if overlap > 0.0:
                            overlap = overlap * self.border_values[obj.i][other.i]/self.perimeter_values[obj.i]
                            xattract = xattract + overlap*(self.x_values[other.i]-self.x_values[obj.i])/dist
                            yattract = yattract + overlap*(self.y_values[other.i]-self.y_values[obj.i])/dist
            
                # Now work out the combined effect of attraction and repulsion 
                atrdst = math.sqrt(xattract * xattract + yattract * yattract)
                repdst = math.sqrt(xrepel * xrepel + yrepel * yrepel)
                if repdst > closest:
                    xrepel = closest * xrepel / (repdst + 1.0)
                    yrepel = closest * yrepel / (repdst + 1.0)
                    repdst = closest
                if repdst > 0.0:
                    xtotal = (1.0-self.ratio) * xrepel + self.ratio*(repdst*xattract/(atrdst + 1.0))
                    ytotal = (1.0-self.ratio) * yrepel + self.ratio*(repdst*yattract/(atrdst + 1.0))
                else:
                    if atrdst > closest:
                        xattract = closest * xattract/(atrdst+1.0)
                        yattract = closest * yattract/(atrdst+1.0)
                    xtotal = xattract
                    ytotal = yattract
                self.x_vectors[obj.i] = self.friction * (self.x_vectors[obj.i] + xtotal)
                self.y_vectors[obj.i] = self.friction * (self.y_vectors[obj.i] + ytotal)
            
            # Update the position for each object
            for obj in self.queryset:
                self.x_values[obj.i] += self.x_vectors[obj.i] + 0.5
                self.y_values[obj.i] += self.y_vectors[obj.i] + 0.5
                obj.circle = Point(
                    self.x_values[obj.i],
                    self.y_values[obj.i],
                ).buffer(obj.radius)
        # Now hand off the results
        self.results = self.queryset

    def add_point(self, pointer, axis, obj):
        if self.tree[pointer]['id'] == 0:
            self.tree[pointer]['id'] = obj.i
            self.tree[pointer]['left'] = 0
            self.tree[pointer]['right'] = 0
            self.tree[pointer]['xpos'] = self.x_values[obj.i]
            self.tree[pointer]['ypos'] = self.y_values[obj.i]
        else:
            if axis == 1:
                if self.x_values[obj.i] >= self.tree[pointer]['xpos']:
                    if self.tree[pointer]['left'] == 0:
                        self.end_pointer += 1
                        self.tree[pointer]['left'] = self.end_pointer
                    self.add_point(self.tree[pointer]['left'], 3-axis, obj)
                else:
                    if self.tree[pointer]['right'] == 0:
                        self.end_pointer += 1
                        self.tree[pointer]['right'] = self.end_pointer
                    self.add_point(self.tree[pointer]['right'], 3-axis, obj)
            else:
                if self.y_values[obj.i] >= self.tree[pointer]['ypos']:
                    if self.tree[pointer]['left'] == 0:
                        self.end_pointer += 1
                        self.tree[pointer]['left'] = self.end_pointer
                    self.add_point(self.tree[pointer]['left'], 3-axis, obj)
                else:
                    if self.tree[pointer]['right'] == 0:
                        self.end_pointer += 1
                        self.tree[pointer]['right'] = self.end_pointer
                    self.add_point(self.tree[pointer]['right'], 3-axis, obj)

    def get_point(self, pointer, axis, obj, distance):
        if pointer > 0:
            if self.tree[pointer]['id'] > 0:
                if axis == 1:
                    if self.x_values[obj.i]-distance < self.tree[pointer]['xpos']:
                        self.get_point(self.tree[pointer]['right'], 3-axis, obj, distance)
                    if self.x_values[obj.i]+distance >= self.tree[pointer]['xpos']:
                        self.get_point(self.tree[pointer]['left'], 3-axis, obj, distance)
                if axis == 2:
                    if self.y_values[obj.i]-distance < self.tree[pointer]['ypos']:
                        self.get_point(self.tree[pointer]['right'], 3-axis, obj, distance)
                    if self.y_values[obj.i]+distance >= self.tree[pointer]['ypos']:
                        self.get_point(self.tree[pointer]['left'], 3-axis, obj, distance)
                if (self.x_values[obj.i]-distance < self.tree[pointer]['xpos'] and
                    self.x_values[obj.i]+distance >= self.tree[pointer]['xpos']):
                    if (self.y_values[obj.i]-distance < self.tree[pointer]['ypos'] and
                        self.y_values[obj.i]+distance >= self.tree[pointer]['ypos']):
                            self.mylist[self.neighbors_within_distance] = self.tree[pointer]['id']
                            self.neighbors_within_distance += 1

