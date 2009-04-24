def get_percent_change(old, new):
	change = new - old
	try:
		percent_change = (change / float(old))*100
		return percent_change
	except ZeroDivisionError:
		return None