def per_sqmi(value, square_miles):
	"""
	Accepts two numbers, a value and an area, and returns the per square mile rate.
	
	Not much more going on here than a simple bit of division.
	
	Fails silents in the case of zero division errors.
	
	h3. Example usage
	
		>> import calculate
		>> calculate.per_sqmi()

	"""
	if not isinstance(value, (int,long,float)):
		return ValueError('Input values should be a number, your first input is a %s' % type(value))
	if not isinstance(square_miles, (int,long,float)):
		return ValueError('Input values should be a number, your second input is a %s' % type(square_miles))
	try:
		rate = float(value) / square_miles
		return rate
	except ZeroDivisionError:
		return None