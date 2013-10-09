def equal_sized_breakpoints(data_list, classes):
    """
    Returns break points for groups of equal size, known as quartiles,
    quintiles, etc.

    Provide a list of data values and the number of classes you'd like the list
    broken up into.

    No flashy math, just sorts them in order and makes the cuts.

    h3. Example usage

        >>> import calculate
        >>> calculate.equal_sized_breakpoints(range(1,101), 5)
        [1.0, 21.0, 41.0, 61.0, 81.0, 100.0]

    """
    # Sort the list
    data_list.sort()

    # Get the total number of values
    n = len(data_list)

    # List where we will stash the break points
    breaks = []

    # Loop through the classes
    for i in range(classes):
        # Get the percentile where this class will cut
        q = i / float(classes)
        # Multiply that by the 'n'
        a = q * n
        # Get the integer version of that number
        aa = int(q * n)
        # Calc the reminder between the two
        r = a - aa
        # Find the value
        breakpoint = (1 - r) * data_list[aa] + r * data_list[aa + 1]
        # Add it to the list
        breaks.append(breakpoint)

    # Tack the final number to the end of the list
    breaks.append(float(data_list[n - 1]))

    # Pass it all out
    return breaks
