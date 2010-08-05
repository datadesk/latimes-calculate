import calculate
from django.contrib.gis.geos import fromstr
from django.contrib.gis.geos import MultiPoint
from django.contrib.gis.db.models.query import GeoQuerySet

def standard_deviation_ellipses(geoqueryset, point_attribute_name='point', 
    num_of_std=1, fix_points=True):
    """
    Accepts a GeoQuerySet and generates one or more standard deviation ellipses
    demonstrating the geospatial distribution of where its points occur.
    
    Returns a one-to-many list of the ellipses as Polygon objects. 
    
    The standard deviation ellipse illustrates the average variation in 
    the distance of points from the mean center, as well as their direction.
    
    By default, the function expects the Point field on your model to be called 'point'.
    
    If the point field is called something else, change the kwarg 'point_attribute_name'
    to whatever your field might be called.
    
    Also by default, the function will nudge slightly apart any identical points and 
    only return the first standard deviation ellipse. If you'd like to change that behavior,
    change the corresponding kwargs.
    
    h3. Example usage
    
        >> import calculate
        >> calculate.standard_deviation_ellipses(qs)
        [<Polygon object at 0x77a1c34>]
    
    h3. Dependencies
    
        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/
        * "psql ellipse() function":http://postgis.refractions.net/support/wiki/index.php?plpgsqlfunctions
    
    h3. Documentation

        * "standard deviation ellipse":http://www.spatialanalysisonline.com/output/html/Directionalanalysisofpointdatasets.html
        * "This code is translated from SQL by Francis Dupont":http://postgis.refractions.net/pipermail/postgis-users/2008-June/020354.html
        
    """
    if not isinstance(geoqueryset, GeoQuerySet):
        raise TypeError('First parameter must be a Django GeoQuerySet. You submitted a %s object' % type(geoqueryset))

    n = len(geoqueryset)
    
    if n < 3:
        return [None]
    
    if fix_points:
        calculate.nudge_points(geoqueryset, point_attribute_name=point_attribute_name)
        
    avg_x = calculate.mean([abs(getattr(p, point_attribute_name).x) for p in geoqueryset])
    avg_y = calculate.mean([abs(getattr(p, point_attribute_name).y) for p in geoqueryset])
    center_x = calculate.mean([getattr(p, point_attribute_name).x for p in geoqueryset])
    center_y = calculate.mean([getattr(p, point_attribute_name).y for p in geoqueryset])
    
    sum_square_diff_avg_x = sum([math.pow((abs(getattr(p, point_attribute_name).x) - avg_x), 2) for p in geoqueryset])
    sum_square_diff_avg_y = sum([math.pow((abs(getattr(p, point_attribute_name).y) - avg_y), 2) for p in geoqueryset])
    sum_diff_avg_x_y = sum([(abs(getattr(p, point_attribute_name).x) - avg_x) * (abs(getattr(p, point_attribute_name).y) - avg_y) for p in geoqueryset])
    sum_square_diff_avg_x_y = sum([math.pow((abs(getattr(p, point_attribute_name).x) - avg_x) * (abs(getattr(p, point_attribute_name).y) - avg_y), 2) for p in geoqueryset])
    constant = math.sqrt(math.pow((sum_square_diff_avg_x - sum_square_diff_avg_y), 2) + (4 * sum_square_diff_avg_x_y))
    theta = math.atan((sum_square_diff_avg_x - sum_square_diff_avg_y + constant) / (2 * sum_diff_avg_x_y))
    
    stdx_sum_x_y_cos_sin_theta = sum([math.pow((((getattr(p, point_attribute_name).x - center_x) * math.cos(theta)) - ((getattr(p, point_attribute_name).y - center_y) * math.sin(theta))), 2) for p in geoqueryset])
    stdy_sum_x_y_sin_cos_theta = sum([math.pow((((getattr(p, point_attribute_name).x - center_x) * math.sin(theta)) - ((getattr(p, point_attribute_name).y - center_y) * math.cos(theta))), 2) for p in geoqueryset])
    
    stdx = math.sqrt((2 * stdx_sum_x_y_cos_sin_theta) / (n - 2))
    stdy = math.sqrt((2 * stdy_sum_x_y_sin_cos_theta) / (n - 2))
    
    results = []
    from django.db import connection
    cursor = connection.cursor()
    while num_of_std:
        cursor.execute("""SELECT ellipse(%s, %s, (%s * %s), (%s * %s), %s, 40);""" % (center_x, center_y, num_of_std, stdx, num_of_std, stdy, theta))
        results.append(fromstr(cursor.fetchall()[0][0], srid=4326))
        num_of_std -= 1
    return results
