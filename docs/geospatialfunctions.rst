Geospatial functions
====================

.. method:: mean_center(obj_list, point_attribute_name='point')

    Accepts a geoqueryset, list of objects or list of dictionaries, expected to contain `GeoDjango Point <https://docs.djangoproject.com/en/dev/ref/contrib/gis/geos/#point>`_ objects as one of their attributes. Returns a Point object with the mean center of the provided points. The mean center is the average x and y of all those points. By default, the function expects the Point field on your model to be called 'point'. If the point field is called something else, change the kwarg 'point_attribute_name' to whatever your field might be called. ::

        >>> import calculate
        >>> calculate.mean_center(qs)
        <Point object at 0x77a1694>

.. method:: nudge_points(geoqueryset, point_attribute_name='point', radius=0.0001)

    A utility that accepts a GeoDjango QuerySet and nudges slightly apart any identical points. Nothing is returned. By default, the distance of the move is 0.0001 decimal degrees. I'm not sure if this will go wrong if your data is in a different unit of measurement. This can be useful for running certain geospatial statistics, or even for presentation issues, like spacing out markers on a Google Map for instance. ::

        >>> import calculate
        >>> calculate.nudge_points(qs)
        >>>

.. method:: random_point(extent)

    A utility that accepts the extent of a polygon and returns a random point from within its boundaries. The extent is a four-point tuple with (xmin, ymin, xmax, ymax). ::

        >>> polygon = Model.objects.get(pk=1).polygon
        >>> import calculate
        >>> calculate.random_point(polygon.extent)

.. method:: standard_deviation_distance(obj_list, point_attribute_name='point')

    Accepts a geoqueryset, list of objects or list of dictionaries, expected to contain objects with Point properties, and returns a float with the standard deviation distance of the provided points. The standard deviation distance is the average variation in the distance of points from the mean center. By default, the function expects the Point field on your model to be called ``point``. If the point field is called something else, change the kwarg ``point_attribute_name`` to whatever your field might be called. ::

        >>> import calculate
        >>> calculate.standard_deviation_distance(qs)
        0.046301584704149731
