def percentage(value, total, multiply=True, fail_silently=True):
    """
    Accepts two integers, a value and a total.

    The value is divided into the total and then multiplied by 100,
    returning its percentage as a float.

    If you don't want the number multiplied by 100, set the 'multiply'
    kwarg to False.

    If you divide into zero -- an illegal operation -- a null value
    is returned by default. If you prefer for an error to be raised,
    set the kwarg 'fail_silently' to False.

    h3. Example usage

        >>> import calculate
        >>> calculate.percentage(2, 10)
        20.0
        >>> calculate.percentage(2,0, multiply=False)
        0.20000000000000001
        >>> calculate.percentage(2,0)
        >>> calculate.percentage(2,0, fail_silently=False)
        ZeroDivisionError

    h3. Documentation

        * "percentage":http://en.wikipedia.org/wiki/Percentage
    """
    try:
        # Divide one into the other
        percent = (value / float(total))
        if multiply:
            # If specified, multiply by 100
            percent = percent * 100
        return percent
    except ZeroDivisionError:
        # If there's a zero involved return null if set to fail silent
        if fail_silently:
            return None
        # but otherwise shout it all out
        else:
            raise ZeroDivisionError("Sorry. You can't divide into zero.")
