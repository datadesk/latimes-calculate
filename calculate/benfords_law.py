from calculate import ptable

def benfords_law(number_list, method='last_digit'):
	"""
	Accepts a list of numbers and applys a quick-and-dirty run against Benford's Law.
	
	This function is incomplete.
	
	h3. Example usage
	
		>> import calculate
		>> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		BENFORD'S LAW: LAST_DIGIT
		| Number | Count | Percentage |
		-------------------------------
		| 0      | 1     | 0.1        |
		| 1      | 1     | 0.1        |
		| 2      | 1     | 0.1        |
		| 3      | 1     | 0.1        |
		| 4      | 1     | 0.1        |
		| 5      | 1     | 0.1        |
		| 6      | 1     | 0.1        |
		| 7      | 1     | 0.1        |
		| 8      | 1     | 0.1        |
		| 9      | 1     | 0.1        |
	
	h3. Sources
	
		"Benford's Law":http://en.wikipedia.org/wiki/Benford%27s_law
		"Applying Benford's Law to CAR":http://www.chasedavis.com/2008/sep/28/applying-benfords-law-car/
		"Benford's Law meets Python and Apple Stock Prices":http://pyevolve.sourceforge.net/wordpress/?p=457
		"Strategic Vision Polls Exhibit Unusual Patterns, Possibly Indicating Fraud":http://www.fivethirtyeight.com/2009/09/strategic-vision-polls-exhibit-unusual.html
		"Nate Silver: pollster may be fraud":http://blogs.tampabay.com/buzz/2009/09/nate-silver-pollster-may-be-fraud.html
		
	
	"""
	# Select the appropriate retrieval method
	if method not in ['last_digit', 'first_digit']:
		raise ValueError('The method you\'ve requested is not included in this function.')
	
	def _get_first_digit(number):
		return int(str(number)[0])
	
	def _get_last_digit(number):
		return int(str(number)[-1])
	
	method_name = '_get_%s' % method
	method_obj = locals()[method_name]

	# Fetch the digits we want to analyze
	digit_list = []
	for number in number_list:
		digit = method_obj(number)
		digit_list.append(digit)
	
	results = []
	for number in xrange(0,10):
		count = digit_list.count(number)
		percentage = count / float(len(digit_list))
		results.append(map(str, [number, count, round(percentage,2)]))
		
	labels = ['Number', 'Count', 'Percentage',]
	print "BENFORD'S LAW: %s" % method.upper()
	print ptable.indent(
		[labels] + results, 
		hasHeader=True, 
		separateRows=False,
		prefix='| ', postfix=' |',
	)