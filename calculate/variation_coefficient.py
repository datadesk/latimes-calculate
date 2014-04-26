import calculate


def variation_coefficient(data_list):
    """
    Accepts a list of values and returns the variation coefficient,
    which is a normalized measure of the distribution.

    This is the sort of thing you can use to compare the standard deviation
    of sets that are measured in different units.

    Note that it uses our "population" standard deviation as part of the
    calculation, not a "sample standard deviation.

    h3. Example usage

        >>> import calculate
        >>> calculate.variation_coefficient([1, 2, -2, 4, -3])
        6.442049363362563

    h3. Documentation

        * "coefficient of variation":http://en.wikipedia.org/wiki/\
Coefficient_of_variation
    """
    # Convert all the values to floats and test to make sure
    # there aren't any strings in there
    try:
        data_list = list(map(float, data_list))
    except ValueError:
        raise ValueError('Input values must contain numbers')
    std = calculate.standard_deviation(data_list)
    mean = calculate.mean(data_list)
    return std / mean
