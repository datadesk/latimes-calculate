def mode(data_list):
    """
    Accepts a sample of numbers and returns the mode value.

    The mode is the most common value in a data set.

    If there is a tie for the highest count, no value is
    returned. The function could be modified to identify
    bimodal results to handle such situations, but I don't
    have a need for it right now so I'm going to leave it
    behind.

    h3. Example usage

        >> import calculate
        >> calculate.mode([1,2,2,3])
        2.0
        >> calculate.mode([1,2,3])
        >>

    h3. Documentation

        "mode":http://en.wikipedia.org/wiki/Mode_(statistics)
    """
    # Convert all the values to floats and test to make sure there
    # aren't any strings in there
    try:
        data_list = list(map(float, data_list))
    except TypeError:
        raise TypeError('Input values must contain numbers')

    # Create a dictionary to store the counts for each value
    counts = {}
    # Loop through the data_list
    for value in data_list:
        if value not in counts:
            # If the value isn't already in the dictionary
            # add it and set it to one.
            counts[value] = 1
        else:
            # And if it is already there, increase the count
            # by one.
            counts[value] += 1

    # Now repurpose the dictionary as a list of tuples so it can be sorted
    sortable_list = [(count, value) for value, count in list(counts.items())]

    # And flip it around...
    sortable_list.sort()

    # ...so that the highest count should appear first
    sortable_list.reverse()

    # If there's only one number, just pass that out
    if len(sortable_list) == 1:
        return sortable_list[0][1]

    # Test to make sure the first and second counts aren't the same
    first_count = sortable_list[0][0]
    second_count = sortable_list[1][0]
    if first_count == second_count:
        # If they are, return None
        return None
    else:
        # If the first count stands above the rest,
        # return it as the mode
        mode = sortable_list[0][1]
        return mode
