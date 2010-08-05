import calculate
from django.contrib.gis.geos import MultiPoint
from django.contrib.gis.db.models.query import GeoQuerySet


def standard_deviation_distance(geoqueryset, point_attribute_name='point'):
    """
    Accepts a geoqueryset, expected to contain objects with Point properties,
    and returns a float with the standard deviation distance of the provided points. 
    
    The standard deviation distance is the average variation in the distance of points 
    from the mean center. 
    
    Unlike a standard deviation ellipse, it does not have a direction.
    
    By default, the function expects the Point field on your model to be called 'point'.
    
    If the point field is called something else, change the kwarg 'point_attribute_name'
    to whatever your field might be called.
    
    h3. Example usage
    
        >> import calculate
        >> calculate.standard_deviation_distance(qs)
        0.046301584704149731
        
    h3. Dependencies
    
        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/
        * "numpy":http://numpy.scipy.org/
        
    h3. Documentation
    
        * "standard deviation distance":http://www.spatialanalysisonline.com/output/html/Directionalanalysisofpointdatasets.html
    
    """
    if not isinstance(geoqueryset, GeoQuerySet):
        raise TypeError('First parameter must be a Django GeoQuerySet. You submitted a %s object' % type(geoqueryset))
    mean = calculate.mean_center(geoqueryset, point_attribute_name=point_attribute_name)
    distances = [getattr(p, point_attribute_name).distance(mean) for p in geoqueryset]
    return calculate.standard_deviation(distances)
