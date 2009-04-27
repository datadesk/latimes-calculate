def percentage(value, total, multiply=True):
	"""
	Accepts two integers, a value and a total. 
	
	The value is divided into the total and then multiplied by 100, 
	returning its percentage as a float.
	
	If you don't want the number multiplied by 100, set the 'multiply'
	kwarg to False.
	
	If one of the numbers is zero, a null value is returned.
	
	h3. Example usage
	
		>> import calculate
		>> calculate.percentage(2, 10)
		20.0
		
	h3. Documentation
	
		* "percentage":http://en.wikipedia.org/wiki/Percentage
	
	"""
	if not isinstance(value, (int,long,float)):
		return ValueError('Input values should be a number, your first input is a %s' % type(value))
	if not isinstance(total, (int,long,float)):
		return ValueError('Input values should be a number, your second input is a %s' % type(total))
	try:
		percent = (value / float(total))
		if multiply:
			percent = percent * 100
		return percent
	except ZeroDivisionError:
		return None