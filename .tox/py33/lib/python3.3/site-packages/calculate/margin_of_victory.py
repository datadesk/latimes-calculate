def margin_of_victory(value_list):
    """
    Accepts a list of numbers and returns the difference between
    the first place and second place values.

    This can be useful for covering elections as an easy to way to figure out
    the margin of victory for a leading candidate.

    h3. Example usage

        >> import calculate
        >> calculate.margin_of_victory([3285, 2804, 7170])
        3885
    """
    # Sort from biggest to smallest
    value_list.sort(reverse=True)

    # Return the difference between the top two values
    return value_list[0] - value_list[1]
