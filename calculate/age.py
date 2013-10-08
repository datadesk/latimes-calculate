from datetime import date, datetime


def age(born, as_of=None):
    """
    Returns the current age, in years, of a person born on the provided date.

    First argument should be the birthdate and can be a datetime.date or
    datetime.datetime object, although datetimes will be converted to a
    date object and hours, minutes and seconds will not be part of the
    calculation.

    The second argument is the `as of` date that the person's age will be
    calculate at. By default, it is not provided and the age is returned as
    of the current date. But if you wanted to calculate someone's age at a
    past or future date, you could do that by providing the `as_of` date
    as the second argument

    Example usage:

        >>> import calculate
        >>> from datetime import datetime
        >>> dob = datetime(1982, 7, 22)
        >>> calculate.age(dob)
        31 # As of this commit!

    Based on code released by Mark at http://stackoverflow.com/a/2259711
    """
    # Set as_of today if it doesn't exist already
    if not as_of:
        as_of = date.today()
    # Get everything into date format
    if isinstance(born, datetime):
        born = born.date()
    if isinstance(as_of, datetime):
        as_of = as_of.date()
    try:
        # raised when birth date is February 29 and the current year
        # is not a leap year
        tmp = born.replace(year=as_of.year)
    except ValueError:
        tmp = born.replace(year=as_of.year, day=born.day - 1)
    if tmp > as_of:
        return as_of.year - born.year - 1
    else:
        return as_of.year - born.year
