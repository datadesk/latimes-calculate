import math

def get_elfi(array):
	"""
	Accepts a list of decimal percentages, which are used 
	to calculate the Ethnolinguistic Fractionalization Index (ELFI).
	
	The list must add up to one.

	The ELFI is a simplified method for calculating the 
	Ethnic Diversity Index. 
	
	Returns a decimal value as a floating point number.
	
	h3. Example usage
	
		>> get_elfi([0.2, 0.5, 0.05, 0.25])
		0.64500000000000002

	h3. Dependencies
	
		* "math":http://docs.python.org/library/math.html
	
	h3. Documentation
	
		* "ethnic diversity index":http://www.ed-data.k12.ca.us/articles/EDITechnical.asp
	
	"""
	if not isinstance(array, list):
		raise TypeError('input must be a list')
	if sum(array) != 1.0:
		raise ValueError('values of submitted array must add up to one. your list adds up to %s' % sum(array))
	elfi = 1 - sum([math.pow(i, 2) for i in array])
	return elfi