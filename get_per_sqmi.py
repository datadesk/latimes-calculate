def get_per_sqmi(value, square_miles):
	try:
		rate = float(value) / square_miles
		return rate
	except ZeroDivisionError:
		return None