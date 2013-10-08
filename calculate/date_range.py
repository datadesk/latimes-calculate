import datetime


def date_range(start_date, end_date):
    """
    Returns a generator of all the days between two date objects.

    Results include the start and end dates.

    Arguments can be either datetime.datetime or date type objects.

    h3. Example usage

        >>> import datetime
        >>> import calculate
        >>> dr = calculate.date_range(
        ...   datetime.date(2009, 1, 1),
        ...   datetime.date(2009, 1, 3),
        ... )
        >>> dr
        <generator object _make at 0x7f5a58437d20>
        >>> list(dr)
        [datetime.date(2009, 1, 1), datetime.date(2009, 1, 2),
            datetime.date(2009, 1, 3)]
    """
    # If a datetime object gets passed in,
    # change it to a date so we can do comparisons.
    if isinstance(start_date, datetime.datetime):
        start_date = start_date.date()
    if isinstance(end_date, datetime.datetime):
        end_date = end_date.date()

    def _make(start_date, end_date):
        # Jump forward from the start_date...
        while True:
            yield start_date
            # ... one day at a time ...
            start_date = start_date + datetime.timedelta(days=1)
            # ... until you reach the end date.
            if start_date > end_date:
                break

    # Verify that the start_date comes after the end_date.
    if start_date > end_date:
        raise ValueError('Provided start_date must come before end_date.')
    else:
        return _make(start_date, end_date)
