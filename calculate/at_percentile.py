import math


def at_percentile(data_list, value, interpolation='fraction'):
    """
    Accepts a list of values and a percentile for which to return the value.

    A percentile of, for example, 80 means that 80 percent of the
    scores in the sequence are below the given score.

    If the requested percentile falls between two values, the result can be
    interpolated using one of the following methods. The default is "fraction".

        1. "fraction"

            The value proportionally between the pair of bordering values.

        2. "lower"

            The lower of the two bordering values.

        3. "higher"

            The higher of the two bordering values.

    h3. Example usage

        >>> import calculate
        >>> calculate.at_percentile([1, 2, 3, 4], 75)
        3.25
        >>> calculate.at_percentile([1, 2, 3, 4], 75, interpolation='lower')
        3.0
        >>> calculate.at_percentile([1, 2, 3, 4], 75, interpolation='higher')
        4.0

    h3. Documentation

        * "Percentile rank":http://en.wikipedia.org/wiki/Percentile_rank

    h3. Credits

        This function is a modification of scipy.stats.scoreatpercentile. The
        only major difference is that I eliminated the numpy dependency.
    """
    # Convert all the values to floats and test to make sure there aren't
    # any strings in there
    try:
        data_list = list(map(float, data_list))
    except ValueError:
        raise ValueError('Input values should contain numbers')

    # Sort the list
    data_list.sort()

    # Find the number of values in the sample
    n = float(len(data_list))

    # Find the index of the provided percentile
    i = ((n - 1) / float(100)) * float(value)

    # Test if that index has a remainder after the decimal point
    remainder = str(i - int(i))[1:]

    # If it doesn't just pull the number at the index
    if remainder == '.0':
        return data_list[int(i)]

    # If it does, interpolate a result using the method provided
    l = data_list[int(math.floor(i))]
    h = data_list[int(math.ceil(i))]
    if interpolation == 'fraction':
        return l + ((h - l) * float(remainder))
    elif interpolation == 'lower':
        return l
    elif interpolation == 'higher':
        return h
    else:
        raise ValueError("The interpolation kwarg must be 'fraction', 'lower' \
or 'higher'. You can also opt to leave it out and rely on the default method.")
