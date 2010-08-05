import math
import random
from operator import attrgetter
from django.contrib.gis.db.models.query import GeoQuerySet


def nudge_points(geoqueryset, point_attribute_name='point', radius=0.0001):
    """
    A utility that accepts a GeoQuerySet and nudges slightly apart any 
    identical points.
    
    Nothing is returned.
    
    By default, the distance of the move is 0.0001 decimal degrees. 
    
    I'm not sure if this will go wrong if your data is in a different unit
    of measurement.
    
    This can be useful for running certain geospatial statistics, or even
    for presentation issues, like spacing out markers on a Google Map for
    instance.
    
    h3. Example usage
    
        >> import calculate
        >> calculate.nudge_points(qs)
        >>
    
    h3. Dependencies
    
        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/
        * "math":http://docs.python.org/library/math.html
    
    h3. Documentation

        * "This code is translated from SQL by Francis Dupont":http://postgis.refractions.net/pipermail/postgis-users/2008-June/020354.html
        
    """
    if not isinstance(geoqueryset, GeoQuerySet):
        raise TypeError('First parameter must be a Django GeoQuerySet. You submitted a %s object' % type(geoqueryset))

    previous_x = None
    previous_y = None
    r = radius 
    for point in sorted(list(geoqueryset), key=attrgetter(point_attribute_name)):
        if getattr(point, point_attribute_name).x == previous_x and getattr(point, point_attribute_name).y == previous_y and previous_x and previous_y:
            theta = random.random() * 2 * math.pi # angle value in radian between 0 and 2pi
            getattr(point, point_attribute_name).x = getattr(point, point_attribute_name).x + (math.cos(theta)*r)
            getattr(point, point_attribute_name).y = getattr(point, point_attribute_name).y + (math.sin(theta)*r)
        else:
            previous_x = getattr(point, point_attribute_name).x
            previous_y = getattr(point, point_attribute_name).y


