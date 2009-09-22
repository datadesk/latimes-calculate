import math
import random
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
	
	# Count all of the distinct points in the geoqueryset
	# by creating a dictionary with the (x, y) coords as 
	# the keys and the counts as the values.
	points_with_counts = {}
	for point in geoqueryset:
		t = (getattr(point, point_attribute_name).x, getattr(point, point_attribute_name).y)
		points_with_counts[t] = points_with_counts.get(t, 0) + 1
	
	# Filter that dictionary down to only those records that appear more than once
	duplicate_points = [point for point, count in points_with_counts.items() if count > 1]
	
	# Abbreviate radius for easier use in equations
	r = radius 
	
	# Loop through the geoqueryset
	for point in geoqueryset:
		
		# Grab the coords in the same manner as above
		t = (getattr(point, point_attribute_name).x, getattr(point, point_attribute_name).y)
	
		# If the coords are in the duplicates...
		if t in duplicate_points:
			# Randomnly calculate the angle value to the move the point in radians between 0 and 2pi
			theta = random.random() * 2 * math.pi 
			# And then shift the point accordingly
			getattr(point, point_attribute_name).x = getattr(point, point_attribute_name).x + (math.cos(theta)*r)
			getattr(point, point_attribute_name).y = getattr(point, point_attribute_name).y + (math.sin(theta)*r)