def split_at_breakpoints(data_list, breakpoint_list):
    """
    Splits up a list at the provided breakpoints.
    
    First argument is a list of data values. Second is a list of the breakpoints
    you'd like it to be split up with.
    
    Returns a list of lists, in order by breakpoint.
    
    Useful for splitting up a list after you've determined breakpoints using
    another method like calculate.equal_sized_breakpoints.

    h3. Example usage

        >>> import calculate
        >>> l = range(1,101)
        >>> bp = calculate.equal_sized_breakpoints(l, 5)
        >>> print bp
        [1.0, 21.0, 41.0, 61.0, 81.0, 100]
        >>> print calculate.split_at_breakpoints(l, bp)
        [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25...

    """
    # Sort the lists
    data_list.sort()
    breakpoint_list.sort()
    
    # Create a list of empty lists that we'll fill in with values as we go along.
    split_list = [[] for i in range(len(breakpoint_list) - 1)]
    
    # Loop through the data list
    for value in data_list:
        
        # Start off by assuming it's in the last break
        group = len(breakpoint_list) - 1
        
        # Then loop through all the breaks from first to last
        for i in range(len(breakpoint_list) - 1):
            # If the value is falls between this break and the next one up...
            if value >= breakpoint_list[i] and value <= breakpoint_list[i + 1]:
                # ...set it as a member of that break
                group = i
        
        # Then add it to the proper list
        split_list[group].append(value)
    
    # Return the list of lists
    return split_list
