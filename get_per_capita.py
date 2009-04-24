def get_percapita(value, population, per=10000):
	try:
		rate = (float(value) / population) * per
		return rate
	except ZeroDivisionError:
		return None