def pareto(data_list):
    """
    =IF (SUM (B$2:B8) > SUM(B$2:B$14)/2, (ABS( SUM(B$2:B$14)/2 - SUM(B$2:B7) ) / B8 ) * D8+C8,"")

    Estimate the mean using grouped data, like we get
    from census age and income distributions.

    Takes a list of data, where each item contains a count of
    the number of items that fall in that range, plus the
    bottom end of the range and it's width.

    Each item should look like this:
        [COUNT, BOTTOM, TOP]

    Here's a full example using age:

    [   # count  # base  # width
        [216350,    0,      5],     # Under 5 years
        [201692,    5,      5],     # 5 to 9 years
        [211151,    10,     5],     # 10 to 14 years
        [204986,    15,     5],     # 15 to 19 years
        [200257,    20,     5],     # 20 to 24 years
        [439047,    25,     10],    # 25 to 34 years
        [459664,    35,     10],    # 35 to 44 years
        [424775,    45,     10],    # 45 to 54 years
        [163492,    55,     5],     # 55 to 59 years
        [127511,    60,     5],     # 60 to 64 years
        [169552,    65,     10],    # 65 to 74 years
        [113693,    75,     10],    # 75 to 84 years
        [44661,     85,     10],    # 85 years and over
    ]

    """
    counts = [float(i[0]) for i in data_list]
    bases = [float(i[1]) for i in data_list]
    widths = [float(i[2]) for i in data_list]

    # break early if we don't have data
    if not counts or sum(counts) == 0:
        return 0

    # Find the group that has the median in it
    # Which will be the group at which the sum of the 
    # cumulative counts is greater than the sum of all
    # of the counts...
    target = sum(counts) / 2
    cumulative_counts = 0
    index = 0
    while cumulative_counts <= target:
        cumulative_counts += counts[index]
        index += 1

    index -= 1
    # Just to be verbose
    median_group_count = counts[index]
    median_group_base = bases[index]
    median_group_width = widths[index]
    # Calculate the sum of all of the groups prior to
    # the one that contains the median 
    previous_groups_sum = cumulative_counts - median_group_count

    # Finally, calculate the median
    median = median_group_base + ((sum(counts)/2 - previous_groups_sum)/median_group_count) * median_group_width
    return median