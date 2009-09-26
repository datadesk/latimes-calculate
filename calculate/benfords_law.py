import math
from calculate import ptable

def benfords_law(number_list, method='first_digit'):
	"""
	Accepts a list of numbers and applies a quick-and-dirty run against Benford's Law.
	
	Benford's Law makes statements about the occurance of leading digits in a dataset.
	It claims that a leading digit of 1 will occur about 30 percent of the time,
	and each number after it a little bit less, with the number 9 occuring the least.
	
	Datasets that greatly vary from the law are sometimes suspected of fraud. 
	
	This function also includes a variation on the classic Benford analysis popularized 
	by blogger Nate Silver, who conducted an analysis of the final digits of polling
	data. To use Silver's variation, provide the keyward argument `method` with the 
	value 'last_digit'.
	
	This function is based upon code from a variety of sources around the web, but
	owes a particular debt to the work of Christian S. Perone.
	
	h3. Example usage
	
		>> import calculate
		>> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		BENFORD'S LAW: FIRST_DIGIT
		| Number | Count | Expected Percentage | Actual Percentage |
		------------------------------------------------------------
		| 1      | 2     | 30.1                | 20.0              |
		| 2      | 1     | 17.61               | 10.0              |
		| 3      | 1     | 12.49               | 10.0              |
		| 4      | 1     | 9.69                | 10.0              |
		| 5      | 1     | 7.92                | 10.0              |
		| 6      | 1     | 6.69                | 10.0              |
		| 7      | 1     | 5.8                 | 10.0              |
		| 8      | 1     | 5.12                | 10.0              |
		| 9      | 1     | 4.58                | 10.0              |
	
	h3. A Warning

	Not all datasets should be expected to conform Benford's rules. 
	I lifted the following guidance from an academic paper linked 
	below.

	Durtschi, Hillison, and Pacini (2004) said Benford "compliance"
	should be expected in the following circumstances:

		1. Numbers that result from mathematical combination of numbers

		2. Transaction-level data (e.g., disbursements, sales) 

		3. Large datasets 

		4. Mean is greater than median and skew is positive 

	And not to expect Benford distributions when:

		1. Numbers are assigned (e.g., check numbers, invoice numbers) 
		
		2. Number influence by human thought (e.g. $1.99)
		
		3. Accounts with a large number of firm-specific numbers 

		4. Accounts with a built-in minimum or maximum 

		5. Where no transaction is recorded.
	
	h3. Sources
	
		"Benford's Law":http://en.wikipedia.org/wiki/Benford%27s_law
		"Applying Benford's Law to CAR":http://www.chasedavis.com/2008/sep/28/applying-benfords-law-car/
		"Breaking the (Benford) Law: Statistical Fraud Detection in Campaign Finance (pdf)":http://cho.pol.uiuc.edu/wendy/papers/tas.pdf
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

	# Set the typical distributions we expect to find
	typical_distributions = { 
		'first_digit': {}, 
		'last_digit': {} 
	}
	for number in xrange(1, 10):
		log10 = math.log10(1+1/float(number))*100.0
		typical_distributions['first_digit'].update({number: log10})
	
	typical_distributions['last_digit'].update({ 
		0: 0.1, 1: 0.1, 2: 0.1, 3: 0.1, 4: 0.1,
		5: 0.1, 6: 0.1, 7: 0.1, 8: 0.1, 9: 0.1,
	})

	# Fetch the digits we want to analyze
	digit_list = []
	for number in number_list:
		digit = method_obj(number)
		digit_list.append(digit)
	
	# Loop through the data set and grab all the applicable numbers
	results = []
	for number in xrange(0,10):
		count = digit_list.count(number)
		try:
			expected_percentage = round(typical_distributions[method][number], 2)
		except KeyError:
			continue
		actual_percentage = round(count / float(len(digit_list)) * 100.0,2)
		results.append(map(str, [number, count, expected_percentage, actual_percentage]))
	
	# Print everything out using our pretty table module
	labels = ['Number', 'Count', 'Expected Percentage', 'Actual Percentage']
	print "BENFORD'S LAW: %s" % method.upper()
	print ptable.indent(
		[labels] + results, 
		hasHeader=True, 
		separateRows=False,
		prefix='| ', postfix=' |',
	)