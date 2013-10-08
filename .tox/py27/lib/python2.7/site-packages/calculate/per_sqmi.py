def per_sqmi(value, square_miles, fail_silently=True):
    """
    Accepts two numbers, a value and an area, and returns the
    per square mile rate.

    Not much more going on here than a simple bit of division.

    If you divide into zero -- an illegal operation -- a null value
    is returned by default. If you prefer for an error to be raised,
    set the kwarg 'fail_silently' to False.

    h3. Example usage

        >> import calculate
        >> calculate.per_sqmi(20, 10)
        2.0
    """
    try:
        return float(value) / square_miles
    except ZeroDivisionError:
        # If there's a zero involved return null if set to fail silent
        if fail_silently:
            return None
        # but otherwise shout it all out
        else:
            raise ZeroDivisionError("Sorry. You can't divide into zero.")
