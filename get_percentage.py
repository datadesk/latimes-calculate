def get_percentage(value, total):
	"""
	Accepts two integers, a value and a total. 
	
	The value is divided into the total and then multiplied by 100, 
	returning its percentage as a float.
	
	If one of the numbers is zero, a null value is returned.
	
	h3. Example usage
	
		>> get_percentage(2, 10)
		20.0
		
	h3. Documentation
	
		* "percentage":http://en.wikipedia.org/wiki/Percentage
	
	"""
	try:
		percent = (value / float(total))*100
		return percent
	except ZeroDivisionError:
		return None