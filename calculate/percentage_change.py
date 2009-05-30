def percentage_change(old_value, new_value, multiply=True):
	"""
	Accepts two integers, an old and a new number, 
	and then measures the percent change between them.
	
	The change between the two numbers is determined 
	and then divided into the original figure. 
	
	By default, it is then multiplied by 100, and 
	returning as a float.
	
	If you don't want the number multiplied by 100, 
	set the 'multiply' kwarg to False.
	
	If one of the numbers is zero, a null value is returned.
	
	h3. Example usage
	
		>> import calculate
		>> calculate.percentage_change(2, 10)
		200.0
		
	h3. Documentation
	
		* "percentage_change":http://en.wikipedia.org/wiki/Percentage_change
	
	"""
	if not isinstance(old_value, (int,long,float)):
		return ValueError('Input values should be a number, your first input is a %s' % type(old_value))
	if not isinstance(new_value, (int,long,float)):
		return ValueError('Input values should be a number, your second input is a %s' % type(new_value))
	change = new_value - old_value
	try:
		percentage_change = (change / float(old_value))
		if multiply:
			percentage_change = percentage_change * 100
		return percentage_change
	except ZeroDivisionError:
		return None