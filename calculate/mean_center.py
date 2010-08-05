from django.contrib.gis.geos import MultiPoint
from django.contrib.gis.db.models.query import GeoQuerySet

def mean_center(geoqueryset, point_attribute_name='point'):
    """
    Accepts a geoqueryset, expected to contain objects with Point properties,
    and returns a Point object with the mean center of the provided points. 
    
    The mean center is the average x and y of all those points. 
    
    By default, the function expects the Point field on your model to be called 'point'.
    
    If the point field is called something else, change the kwarg 'point_attribute_name'
    to whatever your field might be called.
        
    h3. Example usage
    
        >> import calculate
        >> calculate.mean_center(qs)
        <Point object at 0x77a1694>

    h3. Dependencies
    
        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/

    h3. Documentation
        
        * "mean center":http://en.wikipedia.org/wiki/Geostatistics#Descriptive_spatial_statistics
    
    """
    if not isinstance(geoqueryset, GeoQuerySet):
        raise TypeError('First parameter must be a Django GeoQuerySet. You submitted a %s object' % type(geoqueryset))
    multipoint = MultiPoint([getattr(p, point_attribute_name) for p in geoqueryset])
    return multipoint.centroid
