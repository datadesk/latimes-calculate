import datetime

def date_range(start_date, end_date):
	"""
	Returns a generator of all the dates between two datetime objects.
	
	Includes the start and end dates.
	
	h3. Example usage
	
		>>> import calculate
		>>> calculate.date_range(datetime.date(2009,1,1), datetime.date(2009,1,3))
		<generator object at 0x718e90>
		>>> list(calculate.date_range(datetime.date(2009,1,1), datetime.date(2009,1,3)))
		[datetime.date(2009, 1, 1), datetime.date(2009, 1, 2), datetime.date(2009, 1, 3)]
		
	"""
	if start_date > end_date:
		raise ValueError('You provided a start_date that comes after the end_date.')
	while True:
		yield start_date
		start_date = start_date + datetime.timedelta(days=1)
		if start_date > end_date:
			break