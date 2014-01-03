def prorate(value, start_date, end_date, asof_date):
    """
    
    h3. Example usage

        >> import calculate
        >> calculate.per_sqmi(20, 10)
        2.0

    h3. Documentation

        http://en.wikipedia.org/wiki/Pro_rata
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
