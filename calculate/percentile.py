def percentile(data_list, score, kind='weak'):
	"""
	The percentile rank of a score relative to a list of scores.

	A percentile of, for example, 80 percent means that 80 percent of the
	scores in the data_list are below the given score. 
	
	In the case of gaps or ties, the exact definition depends on the type
	of the calculation stipulated by the kind keyword argument.
	
	This function is a modification of scipy.stats.percentileofscore. The 
	only major difference is that I eliminated the numpy dependency, and
	omitted the rank kwarg option until I can get more time to translate
	the numpy parts out.

	h3. Parameters
	
		* data_list: list
			
			* A list of scores to which the score argument is compared.
	
		* score: int or float
			
			* Value that is compared to the elements in the data_list.
			
		* kind: {'rank', 'weak', 'strict', 'mean'}, optional
		
			* This optional parameter specifies the interpretation of the resulting score:

				* "weak": This kind corresponds to the definition of a cumulative
						  distribution function.  A percentileofscore of 80%
						  means that 80% of values are less than or equal
						  to the provided score.
				
				* "strict": Similar to "weak", except that only values that are
							strictly less than the given score are counted.
				
				* "mean": The average of the "weak" and "strict" scores, often used in
						  testing.	See
	
	h3. Documentation
	
		* "Percentile rank":http://en.wikipedia.org/wiki/Percentile_rank
		* "scipy.stats":http://www.scipy.org/SciPyPackages/Stats

	Example usage::

		Three-quarters of the given values lie below a given score:

			>>> percentileofscore([1, 2, 3, 4], 3)
			75.0

		Only 2/5 values are strictly less than 3:

			>>> percentile([1, 2, 3, 3, 4], 3, kind='strict')
			40.0

		But 4/5 values are less than or equal to 3:

			>>> percentile([1, 2, 3, 3, 4], 3, kind='weak')
			80.0

		The average between the weak and the strict scores is

			>>> percentile([1, 2, 3, 3, 4], 3, kind='mean')
			60.0

	"""
	n = len(data_list)

	if kind == 'strict':
		return len([i for i in data_list if i < score]) / float(n) * 100
	elif kind == 'weak':
		return len([i for i in data_list if i <= score]) / float(n) * 100
	elif kind == 'mean':
		return (len([i for i in data_list if i < score]) + len([i for i in data_list if i <= score])) * 50 / float(n)
	else:
		raise ValueError("The kind kwarg must be 'strict', 'weak' or 'mean'. You can also opt to leave it out and rely on the default method.")