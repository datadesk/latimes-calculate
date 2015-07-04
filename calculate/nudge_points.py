import math
import random
from operator import attrgetter
from django.contrib.gis.geos import Point


def nudge_points(geoqueryset, point_attribute_name='point', radius=0.0001):
    """
    A utility that accepts a list of objects with a GeoDjango Point attribute
    and nudges slightly apart any identical points.

    Returns the modified input as a list.

    By default it looks for the point in an attribute named "point." If
    your point data attribute has a different name, submit it as a string
    to the "point_attribute_name" kwarg.

    By default, the distance of the move is 0.0001 decimal degrees. You can
    mofied it by submitting a "radius" kwarg.

    I'm not sure if this will go wrong if your data is in a different unit
    of measurement.

    This can be useful for running certain geospatial statistics, or even
    for presentation issues, like spacing out markers on a Google Map for
    instance.

    h3. Example usage

        >>> import calculate
        >>> from models import FakePoint
        >>> qs = FakePoint.objects.all()
        >>> qs = calculate.nudge_points(qs)

    h3. Dependencies

        * "django":http://www.djangoproject.com/
        * "geodjango":http://www.geodjango.org/
        * "math":http://docs.python.org/library/math.html

    h3. Documentation

        * "This code is translated from SQL by Francis Dupont":http://postgis.\
refractions.net/pipermail/postgis-users/2008-June/020354.html
    """
    previous_x = None
    previous_y = None
    r = radius
    pan = point_attribute_name
    sorted_gqs = sorted(list(geoqueryset), key=attrgetter(pan))

    out_list = []
    for obj in sorted_gqs:
        x = getattr(obj, pan).x
        y = getattr(obj, pan).y
        if (x == previous_x and y == previous_y and
                previous_x is not None and previous_y is not None):
            # angle value in radian between 0 and 2pi
            theta = random.random() * 2 * math.pi
            new_point = Point(
                x + (math.cos(theta) * r),
                y + (math.sin(theta) * r)
            )
            setattr(obj, pan, new_point)
        else:
            previous_x = x
            previous_y = y
        out_list.append(obj)
    return out_list
