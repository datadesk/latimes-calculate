import math
import calculate

def standard_deviation(data_list):
	"""
	Returns the standard deviation of a list of numbers.
	
	h3. Documentation
	
		http://en.wikipedia.org/wiki/Standard_deviation
	
	"""
	data_list = map(float, data_list)
	mean = calculate.mean(data_list)
	deviations = [i - mean for i in data_list]
	deviations_squared = [math.pow(i, 2) for i in deviations]
	mean_deviation = calculate.mean(deviations_squared)
	standard_deviation = math.sqrt(mean_deviation)
	return standard_deviation