import calculate


def percentile(data_list, value, kind='weak'):
    """
    Accepts a sample of values and a single number to compare to it
    and determine its percentile rank.

    A percentile of, for example, 80 means that 80 percent of the
    scores in the sequence are below the given score.

    In the case of gaps or ties, the exact definition depends on the type
    of the calculation stipulated by the "kind" keyword argument.

    There are three kinds of percentile calculations provided here. The
    default is "weak".

        1. "weak"

            Corresponds to the definition of a cumulative
            distribution function, with the result generated
            by returning the percentage of values at or equal
            to the the provided value.

        2. "strict"

            Similar to "weak", except that only values that are
            less than the given score are counted. This can often
            produce a result much lower than "weak" when the provided
            score is occurs many times in the sample.

        3. "mean"

            The average of the "weak" and "strict" scores.

    h3. Example usage

        >> import calculate
        >> calculate.percentile([1, 2, 3, 4], 3)
        75.0
        >> calculate.percentile([1, 2, 3, 3, 4], 3, kind='strict')
        40.0
        >> calculate.percentile([1, 2, 3, 3, 4], 3, kind='weak')
        80.0
        >> calculate.percentile([1, 2, 3, 3, 4], 3, kind='mean')
        60.0

    h3. Documentation

        * "Percentile rank":http://en.wikipedia.org/wiki/Percentile_rank

    h3. Credits

        This function is a modification of scipy.stats.percentileofscore. The
        only major difference is that I eliminated the numpy dependency, and
        omitted the rank kwarg option until I can find time to translate
        the numpy parts out.
    """
    # Convert all the values to floats and test to make sure
    # there aren't any strings in there
    try:
        data_list = list(map(float, data_list))
    except ValueError:
        raise ValueError('Input values should contain numbers, your first \
input contains something else')

    # Find the number of values in the sample
    n = float(len(data_list))

    if kind == 'strict':
        # If the selected method is strict, count the number of values
        # below the provided one and then divide it into the n
        return len([i for i in data_list if i < value]) / n * 100

    elif kind == 'weak':
        # If the selected method is weak, count the number of values
        # equal to or below the provided on and then divide it into n
        return len([i for i in data_list if i <= value]) / n * 100

    elif kind == 'mean':
        # If the selected method is mean, take the weak and strong
        # methods and average them.
        strict = len([i for i in data_list if i < value]) / n * 100
        weak = len([i for i in data_list if i <= value]) / n * 100
        return calculate.mean([strict, weak])
    else:
        raise ValueError("The kind kwarg must be 'strict', 'weak' or 'mean'. \
You can also opt to leave it out and rely on the default method.")
