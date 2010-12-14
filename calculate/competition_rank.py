from django.db.models.query import QuerySet


def competition_rank(queryset, obj, order_by, direction='desc'):
    """
    Accepts a Django queryset and a Django object, the value and direction
    to order by, returns the object's competition rank as an integer.
    
    In competition ranking equal numbers receive the same ranking and a gap
    is left before the next value (i.e. "1224").
    
    h3. Example usage
    
        >> import calculate
        >> qs = Player.objects.all().order_by("-career_home_runs")
        >> ernie = Player.objects.get(first_name__iexact='Ernie', last_name__iexact='Banks')
        >> eddie = Player.objects.get(first_name__iexact='Eddie', last_name__iexact='Matthews')
        >> mel = Player.objects.get(first_name__iexact='Mel', last_name__iexact='Ott')
        >> calculate.competition_rank(qs, ernie, order_by='career_home_runs', direction='desc')
        21
        >> calculate.competition_rank(qs, eddie, order_by='career_home_runs', direction='desc')
        21
        >> calculate.competition_rank(qs, mel, order_by='career_home_runs', direction='desc')
        23
    
    h3. Dependencies
    
        * "django":http://www.djangoproject.com/
    
    h3. Documentation
    
        * "standard competition rank":http://en.wikipedia.org/wiki/Ranking#Standard_competition_ranking_.28.221224.22_ranking.29
    
    """
    if not isinstance(queryset, QuerySet):
        raise TypeError('First parameter must be a Django QuerySet. You submitted a %s object' % type(queryset))
    if direction == 'desc':
        order_value = '-' + order_by
    elif direction == 'asc':
        order_value = order_by
    else:
        raise ValueError('Direction kwarg should be either asc or desc. You submitted %s' % direction)
    queryset = queryset.order_by(order_value)
    rank = 0
    tie_count = 1
    for i, x in enumerate(queryset):
        if i != 0 and getattr(queryset[i], order_by) == getattr(queryset[i-1], order_by):
            tie_count += 1
        else:
            rank = rank + tie_count
            tie_count = 1
        if obj == x:
            return rank
