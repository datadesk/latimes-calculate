def mean(data_list):
    """
    Accepts a sample of values and returns their mean.

    The mean is the sum of all values in the sample divided by
    the number of members. It is also known as the average.

    Since the value is strongly influenced by outliers, median
    is generally a better indicator of central tendency.

    h3. Example usage

        >> import calculate
        >> calculate.mean([1,2,3])
        2.0
        >> calculate.mean([1, 99])
        50.0

    h3. Documentation

        "mean":http://en.wikipedia.org/wiki/Arithmetic_mean
    """
    # Convert all the values to floats and test to make sure
    # there aren't any strings in there
    try:
        data_list = list(map(float, data_list))
    except ValueError:
        raise ValueError('Input values should contain numbers')
    # Count the number of values in the sample
    n = len(data_list)
    # Sum up the values in the sample
    sum_ = sum(data_list)
    # Divide them to find the mean
    return sum_ / n
