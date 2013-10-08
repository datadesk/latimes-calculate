import random
from django.contrib.gis.geos import Point


def random_point(extent):
    """
    A utility that accepts the extent of a polygon and returns a random
    point from within its boundaries.

    The extent is a four-point tuple with (xmin, ymin, xmax, ymax).

    h3. Example usage

        >> polygon = Model.objects.get(pk=1).polygon
        >> import calculate
        >> calculate.random_point(polygon.extent)

    h3. Dependencies

        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/
        * "random":http://docs.python.org/library/random.html

    h3. Documentation

        * "extent":http://geodjango.org/docs/geos.html#extent
        * "Code lifted from Joost at DjangoDays":http://djangodays.com/\
2009/03/04/geodjango-getting-a-random-point-within-a-multipolygon/
    """
    xmin, ymin, xmax, ymax = extent
    xrange = xmax - xmin
    yrange = ymax - ymin
    randx = xrange * random.random() + xmin
    randy = yrange * random.random() + ymin
    return Point(randx, randy)
