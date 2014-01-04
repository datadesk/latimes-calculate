def ordinal_rank(sequence, item, order_by=None, direction='desc'):
    """
    Accepts a list and an object. Returns the object's ordinal rank
    as an integer.

    h3. Example usage

        >> import calculate
        >> qs = Player.objects.all().order_by("-career_home_runs")
        >> barry = Player.objects.get(
            first_name__iexact='Barry',
            last_name__iexact='Bonds'
        )
        >> calculate.ordinal_rank(list(qs), barry)
        1

    h3. Documentation

        * "ordinal rank":http://en.wikipedia.org/wiki/Ranking#Ordinal_ranking\
_.28.221234.22_ranking.29
    """
    seq_list = list(sequence)
    if order_by:
        # Figure out what type of objects we're dealing with
        if isinstance(seq_list[0], type({})):
            def getkey(obj, key):
                return obj.get(key)
            gettr = getkey
        else:
            gettr = getattr
        if direction == 'desc':
            seq_list.sort(key=lambda x: gettr(x, order_by), reverse=True)
        elif direction == 'asc':
            seq_list.sort(key=lambda x: gettr(x, order_by))
        else:
            raise ValueError('Direction kwarg should be either asc or desc.')
    index = seq_list.index(item)
    return index + 1
