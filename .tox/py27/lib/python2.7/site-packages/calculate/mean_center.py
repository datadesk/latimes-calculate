from django.contrib.gis.geos import MultiPoint


def mean_center(obj_list, point_attribute_name='point'):
    """
    Accepts a geoqueryset, list of objects or list of dictionaries, expected
    to contain GeoDjango Point objects as one of their attributes.

    Returns a Point object with the mean center of the provided points.

    The mean center is the average x and y of all those points.

    By default, the function expects the Point field on your model
    to be called 'point'.

    If the point field is called something else, change the kwarg
    'point_attribute_name' to whatever your field might be called.

    h3. Example usage

        >> import calculate
        >> calculate.mean_center(qs)
        <Point object at 0x77a1694>

    h3. Dependencies

        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/

    h3. Documentation

        * "mean center":http://help.arcgis.com/en/arcgisdesktop/10.0/help/\
index.html#//005p00000018000000.htm

    """
    # Figure out what type of objects we're dealing with
    if isinstance(obj_list[0], type({})):
        def getkey(obj, key):
            return obj.get(key)
        gettr = getkey
    else:
        gettr = getattr
    # Crunch it
    multipoint = MultiPoint([gettr(p, point_attribute_name) for p in obj_list])
    return multipoint.centroid
