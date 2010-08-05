import math

def elfi(data_list):
    """
    The ELFI is a simplified method for calculating the 
    Ethnic Diversity Index. 
    
    Accepts a list of decimal percentages, which are used 
    to calculate the Ethnolinguistic Fractionalization Index (ELFI).
    
    Returns a decimal value as a floating point number.
    
    h3. Example usage
    
        >>> import calculate
        >> calculate.elfi([0.2, 0.5, 0.05, 0.25])
        0.64500000000000002
    
    h3. Dependencies
    
        * "math":http://docs.python.org/library/math.html
    
    h3. Documentation
    
        * "ethnic diversity index":http://www.ed-data.k12.ca.us/articles/EDITechnical.asp
    
    """
    # Test to make sure the input is a list or tuple
    if not isinstance(data_list, (list, tuple)):
        raise TypeError('First input must be a list or tuple. You input a %s' % type(data_list))

    # Convert all the values to floats and test to make sure there aren't any strings in there
    try:
        data_list = map(float, data_list)
    except ValueError:
        raise ValueError('Input values should contain numbers, your first input contains something else')

    # Calculate the ELFI
    elfi = 1 - sum([math.pow(i, 2) for i in data_list])
    return elfi
