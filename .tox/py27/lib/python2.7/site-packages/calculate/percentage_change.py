def percentage_change(old_value, new_value, multiply=True, fail_silently=True):
    """
    Accepts two integers, an old and a new number,
    and then measures the percent change between them.

    The change between the two numbers is determined
    and then divided into the original figure.

    By default, it is then multiplied by 100, and
    returning as a float.

    If you don't want the number multiplied by 100,
    set the 'multiply' kwarg to False.

    If you divide into zero -- an illegal operation -- a null value
    is returned by default. If you prefer for an error to be raised,
    set the kwarg 'fail_silently' to False.

    h3. Example usage

        >> import calculate
        >> calculate.percentage_change(2, 10)
        400.0

    h3. Documentation

        * "percentage_change":http://en.wikipedia.org/wiki/Percentage_change
    """
    change = new_value - old_value
    try:
        percentage_change = (change / float(old_value))
        if multiply:
            percentage_change = percentage_change * 100
        return percentage_change
    except ZeroDivisionError:
        # If there's a zero involved return null if set to fail silent
        if fail_silently:
            return None
        # but otherwise shout it all out
        else:
            raise ZeroDivisionError("Sorry. You can't divide into zero.")
