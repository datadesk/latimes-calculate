import calculate


def decile(data_list, score, kind='weak'):
    """
    Accepts a sample of values and a single number to add to it
    and determine the decile equivilent of its percentile rank.

    By default, the method used to negotiate gaps and ties
    is "weak" because it returns the percentile of all values
    at or below the provided value. For an explanation of
    alternative methods, refer to the calculate.percentile
    function.

    h3. Example usage

        >> import calculate
        >> calculate.decile([1, 2, 3, 3, 4], 3)
        9

    h3. Documentation

        * "percentile rank":http://en.wikipedia.org/wiki/Percentile_rank
        * "decile":http://en.wikipedia.org/wiki/Decile

    """
    # Use calculate.percentile to fetch the precise percentile
    # ranking of the desired value
    percentile_score = calculate.percentile(data_list, score, kind=kind)

    # Now translate that value to a decile value
    if percentile_score == 100.0:
        # If the value is 100, it's easy, return 10
        return 10
    else:
        # Otherwise, reduce the value to single digits,
        # shave off the decimal by converting it to an
        # integer, and then add one, so that, for example,
        # 0.X numbers are in the first decile, and 9.X
        # numbers are in the 10th. - where we want them.
        decile = int(percentile_score * 0.1) + 1
        return decile
