def range(data_list):
    """
    Accepts a sample of values and return the range.

    The range is the difference between the maximum and
    minimum values of a data set.

    h3. Example usage

        >> import calculate
        >> calculate.range([1,2,3])
        2
        >> calculate.range([2,2])
        0

    h3. Documentation

        "range":http://en.wikipedia.org/wiki/Range_(statistics)
    """
    # Convert all the values to floats and test to make sure
    # there aren't any strings in there
    try:
        data_list = list(map(float, data_list))
    except ValueError:
        raise ValueError('Input values should contain numbers, your first \
            input contains something else')

    # Make sure the sample has more than one entry
    if len(data_list) < 2:
        raise ValueError('Input must contain at least two values. \
            You provided a list with %s values' % len(data_list))

    # Find the maximum value in the list
    max_ = max(data_list)

    # Find the minimum value in the list
    min_ = min(data_list)

    # Find the range by calculating the difference
    return max_ - min_
