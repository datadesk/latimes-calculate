

def competition_rank(obj_list, obj, order_by, direction='desc'):
    """
    Accepts a list, an item plus the value and direction
    to order by. Then returns the supplied object's competition rank as an integer.
    
    In competition ranking equal numbers receive the same ranking and a gap
    is left before the next value (i.e. "1224").
    
    You can submit a Django queryset, objects, or just dictionaries.
    
    h3. Example usage
    
        >> import calculate
        >> qs = Player.objects.all().order_by("-career_home_runs")
        >> ernie = Player.objects.get(first_name__iexact='Ernie', last_name__iexact='Banks')
        >> eddie = Player.objects.get(first_name__iexact='Eddie', last_name__iexact='Matthews')
        >> mel = Player.objects.get(first_name__iexact='Mel', last_name__iexact='Ott')
        >> calculate.competition_rank(qs, ernie, career_home_runs', direction='desc')
        21
        >> calculate.competition_rank(qs, eddie, 'career_home_runs', direction='desc')
        21
        >> calculate.competition_rank(qs, mel, 'career_home_runs', direction='desc')
        23
    
    h3. Documentation
    
        * "standard competition rank":http://en.wikipedia.org/wiki/Ranking#Standard_competition_ranking_.28.221224.22_ranking.29
    
    """
    # Convert the object list to a list type, in case it's a Django queryset
    obj_list = list(obj_list)
    
    # Validate the direction
    if direction not in ['desc', 'asc']:
        raise ValueError('Direction kwarg should be either asc or desc. You submitted %s' % direction)
    
    # Figure out what type of objects we're dealing with
    if type(obj_list[0]) == type({}):
        def getkey(obj, key):
            return obj.get(key)
        gettr = getkey
    else:
        gettr = getattr
    
    # Reorder list
    if direction == 'desc':
        obj_list.sort(key=lambda x:gettr(x, order_by), reverse=True)
    elif direction == 'asc':
        obj_list.sort(key=lambda x: gettr(x, order_by))
    rank = 0
    tie_count = 1
    for i, x in enumerate(obj_list):
        if i != 0 and gettr(obj_list[i], order_by) == gettr(obj_list[i-1], order_by):
            tie_count += 1
        else:
            rank = rank + tie_count
            tie_count = 1
        if obj == x:
            return rank
            
            
            
