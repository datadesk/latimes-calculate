from types import FunctionType


def competition_rank(obj_list, obj, order_by, direction='desc'):
    """
    Accepts a list, an item plus the value and direction
    to order by. Then returns the supplied object's competition rank
    as an integer.

    In competition ranking equal numbers receive the same ranking and a gap
    is left before the next value (i.e. "1224").

    h3. Example usage

        >> import calculate
        >> qs = list(Player.objects.all().order_by("-career_home_runs"))
        >> ernie = Player.objects.get(name='Ernie Banks')
        >> eddie = Player.objects.get(name='Eddie Matthews')
        >> calculate.competition_rank(
            qs,
            ernie,
            'career_home_runs',
            direction='desc'
        )
        21
        >> calculate.competition_rank(
            qs,
            eddie,
            'career_home_runs',
            direction='desc'
        )
        21

    h3. Documentation

        * "standard competition rank":http://en.wikipedia.org/wiki/Ranking#\
Standard_competition_ranking_.28.221224.22_ranking.29
    """
    # Convert the object list to a list type, in case it's a Django queryset
    obj_list = list(obj_list)

    # Validate the direction
    if direction not in ['desc', 'asc']:
        raise ValueError('Direction kwarg should be either asc or desc.')

    # Figure out what type of objects we're dealing with
    # and assign the proper way of accessing them.

    # If we've passed in a lambda or function as
    # our order_by, we need to act accordingly.
    if isinstance(order_by, FunctionType):
        def getfunc(obj, func):
            return func(obj)
        gettr = getfunc
    # If the objects are dicts we'll need to pull keys
    elif isinstance(obj_list[0], type({})):
        def getkey(obj, key):
            return obj.get(key)
        gettr = getkey
    # ... otherwise just assume the list is full of objects with attributes
    else:
        gettr = getattr

    # Reorder list
    if direction == 'desc':
        obj_list.sort(key=lambda x: gettr(x, order_by), reverse=True)
    elif direction == 'asc':
        obj_list.sort(key=lambda x: gettr(x, order_by))

    # Set up some globals
    rank = 0
    tie_count = 1

    # Loop through the list
    for i, x in enumerate(obj_list):
        # And keep counting ...
        if (i != 0 and
                gettr(obj_list[i], order_by) ==
                gettr(obj_list[i - 1], order_by)):
            tie_count += 1
        else:
            rank = rank + tie_count
            tie_count = 1
        # ... Until we hit the submitted object
        if obj == x:
            return rank
