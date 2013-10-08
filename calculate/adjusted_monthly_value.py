import six
import calendar
import datetime


def adjusted_monthly_value(value, dt):
    """
    Accepts a value and a datetime object, and then prorates the value to a
    30-day figure depending on how many days are in the month.

    This can be useful for month-to-month comparisons in circumstances where
    fluctuations in the number of days per month may skew the analysis.

    For instance, February typically has only 28 days, in comparison to March,
    which has 31.

    h3. Example usage

        >> import calculate
        >> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 4, 1))
        10.0
        >> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 2, 17))
        10.714285714285714
        >> calculate.adjusted_monthly_value(
            10,
            datetime.datetime(2009, 12, 31)
        )
        9.67741935483871

    h3. Documentation

        "calendar module":http://docs.python.org/library/calendar.html
    """
    # Test to make sure the first input is a number
    if not isinstance(value, six.integer_types):
        raise TypeError('Input values should be a number')

    # Test to make sure the second input is a date
    if not isinstance(dt, (datetime.datetime, datetime.date)):
        raise TypeError('You must submit a date or datetime value')

    # Get the length of the month
    length_of_month = calendar.monthrange(dt.year, dt.month)[1]

    # Determine the adjustment necessary to pro-rate the value to 30 days.
    adjustment = 30.0 / length_of_month

    # Multiply the value against the adjustment and return the result
    return value * adjustment
