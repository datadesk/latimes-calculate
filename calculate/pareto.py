def pareto_median(data_list):
    """
    This is a python port of a formula by Steve Doig,
    Bob Hoyer and Meghan Hoyer.
    
    It estimates the median of grouped/range data, like we get
    from census age and income distributions (n number of
    people are between 5 and 10 years old).

    This function takes a list of data groups. Each item in the
    list should correspond to a range like:
        [
            [count of items in the range, base or lower bound],
        ]

    Here's a full example using age data from the census:

    >>> ages = [
    >>>     [216350, 0],  # Under 5 years
    >>>     [201692, 5],  # 5 to 9 years
    >>>     [211151, 10], # 10 to 14 years
    >>>     [204986, 15], # 15 to 19 years
    >>>     [200257, 20], # 20 to 24 years
    >>>     [439047, 25], # 25 to 34 years
    >>>     [459664, 35], # 35 to 44 years
    >>>     [424775, 45], # 45 to 54 years
    >>>     [163492, 55], # 55 to 59 years
    >>>     [127511, 60], # 60 to 64 years
    >>>     [169552, 65], # 65 to 74 years
    >>>     [113693, 75], # 75 to 84 years
    >>>     [44661, 85],  # 85 years and over
    >>> ]
    >>> pareto_median(ages)
    35.3

    And, finally, an explanation from Steve Doig on how this all
    works, using the above sample data:

    "The total population is 2,976,831, so the midpoint of the
    population is 2,976,831/2=1,488,416. That value falls into
    the 35 to 44 years range, which begins with 1,473,483 counted
    in ages 0-34. There are 459,664 people in the 35-44 range.
    The midpoint is 1,488,416-1,473,483 = 14,933 people into the
    range. As a decimal, it is 14,933/459,664 = 0.032 into the range.
    The 35-44 range is 10 years wide. 35+(0.032*10) = 35.3 years"

    """
    # First make sure our list is in ascending order
    data_list = sorted(data_list, key=lambda lst: lst[1])
    
    # Pull out our elements into separate lists to make
    # things clearer later on. Cast them as floats now 
    # to avoid possible coercion bugs later.
    counts = [float(i[0]) for i in data_list]
    bases = [float(i[1]) for i in data_list]
    
    # break early if we don't have data
    if not counts or sum(counts) == 0:
        return 0
    
    # Now, we need to calculate the "widths" of each group.
    # Basicaly, it's the number of units (years, dollars, etc)
    # each group covers. 20,000-25,000 would be 5,000.
    widths = []
    for index, value in enumerate(bases):
        # Since the last item in most ranges has no upward bound
        # by definition, this value can be tricky to calculate.
        # It shouldn't matter unless the median is the in the final
        # grouping -- which should be rare -- but in that case, you
        # may want to find a different way to estimate the median.
        try:
            val = bases[index + 1] - bases[index]
        except IndexError:
            val = 1
        widths.append(val)
    
    # Find the group that has the median in it
    # Which will be the group at which the sum of the 
    # cumulative counts is greater than the sum of all
    # of the counts divided by 2...
    target = sum(counts) / 2
    cumulative_counts = 0
    index = 0
    while cumulative_counts <= target:
        cumulative_counts += counts[index]
        index += 1
    
    index -= 1
    # Calculate the sum of all of the groups prior to
    # the one that contains the median 
    previous_groups_sum = cumulative_counts - counts[index]
    # Finally, estimate the median
    return bases[index] + ((sum(counts)/2 - previous_groups_sum)/counts[index]) * widths[index]
