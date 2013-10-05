import calculate


def standard_deviation_distance(obj_list, point_attribute_name='point'):
    """
    Accepts a geoqueryset, list of objects or list of dictionaries, expected
    to contain objects with Point properties, and returns a float with the
    standard deviation distance of the provided points.

    The standard deviation distance is the average variation in the distance
    of points from the mean center.

    Unlike a standard deviation ellipse, it does not have a direction.

    By default, the function expects the Point field on your model to be
    called 'point'.

    If the point field is called something else, change the kwarg
    'point_attribute_name' to whatever your field might be called.

    h3. Example usage

        >> import calculate
        >> calculate.standard_deviation_distance(qs)
        0.046301584704149731

    h3. Dependencies

        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/

    h3. Documentation

        * "standard deviation distance":http://www.spatialanalysisonline.com/\
output/html/Directionalanalysisofpointdatasets.html
    """
    # Figure out what type of objects we're dealing with
    if isinstance(obj_list[0], type({})):
        def getkey(obj, key):
            return obj.get(key)
        gettr = getkey
    else:
        gettr = getattr
    mean = calculate.mean_center(
        obj_list,
        point_attribute_name=point_attribute_name
    )
    distances = [
        gettr(p, point_attribute_name).distance(mean)
        for p in obj_list
    ]
    return calculate.standard_deviation(distances)
