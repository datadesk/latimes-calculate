import math
import calculate

def standard_deviation(data_list):
    """
    Accepts a sample of values and returns the standard deviation.
    
    Standard deviation measures how widely dispersed the values are
    from the mean. A lower value means the data tend to be bunched
    close to the averge. A higher value means they tend to be further 
    away.
    
    h3. Example usage
    
        >> import calculate
        >>> calculate.standard_deviation([2,3,3,4])
        0.70710678118654757
        >>> calculate.standard_deviation([-2,3,3,40])
        16.867127793432999
    
    h3. Documentation
    
        "standard deviation":http://en.wikipedia.org/wiki/Standard_deviation
    
    """
    # Convert all the values to floats and test to make sure there aren't any strings in there
    try:
        data_list = map(float, data_list)
    except ValueError:
        raise ValueError('Input values should contain numbers, your first input contains something else')
    
    # Find the mean
    mean = calculate.mean(data_list)
    
    # Create a new list containing the distance from mean for each value in the sample
    deviations = [i - mean for i in data_list]
    
    # Square the distances
    deviations_squared = [math.pow(i, 2) for i in deviations]
    
    # Take the average of those squares
    mean_deviation = calculate.mean(deviations_squared)
    
    # And then take the square root of the mean to find the standard deviation
    return math.sqrt(mean_deviation)
