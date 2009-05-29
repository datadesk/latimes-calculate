def median(data_list):
	"""
	Finds the median in a list of numbers.
	"""
	data_list = map(float, data_list)
	n = len(data_list)
	data_list.sort()
	print data_list
	# Test whether the n is odd
	if n & 1:
		# If is is, get the index simply by dividing it in half
		index = n / 2 
		return data_list[index]
	else:
		# If the n is even, average the two values at the center
		print "EVEN!"
		low_index = n / 2 - 1
		print low_index
		high_index = n / 2
		print high_index
		average = (data_list[low_index] + data_list[high_index]) / 2
		return average
