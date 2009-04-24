def get_per_capita(value, population, per=10000):
	try:
		rate = (float(value) / population) * per
		return rate
	except ZeroDivisionError:
		return None