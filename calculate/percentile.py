"""
This script is lifted from scipy.stats.percentileofscore

http://www.scipy.org/SciPyPackages/Stats
"""
import numpy as np

def percentile(a, score, kind='rank'):
	'''
	The percentile rank of a score relative to a list of scores.

	A `percentileofscore` of, for example, 80% means that 80% of the
	scores in `a` are below the given score. In the case of gaps or
	ties, the exact definition depends on the optional keyword, `kind`.

	Parameters
	----------
	a: array like
		Array of scores to which `score` is compared.
	score: int or float
		Score that is compared to the elements in `a`.
	kind: {'rank', 'weak', 'strict', 'mean'}, optional
		This optional parameter specifies the interpretation of the
		resulting score:

		- "rank": Average percentage ranking of score.	In case of
				  multiple matches, average the percentage rankings of
				  all matching scores.
		- "weak": This kind corresponds to the definition of a cumulative
				  distribution function.  A percentileofscore of 80%
				  means that 80% of values are less than or equal
				  to the provided score.
		- "strict": Similar to "weak", except that only values that are
					strictly less than the given score are counted.
		- "mean": The average of the "weak" and "strict" scores, often used in
				  testing.	See

				  http://en.wikipedia.org/wiki/Percentile_rank

	Returns
	-------
	pcos : float
		Percentile-position of score (0-100) relative to `a`.

	Examples
	--------
	Three-quarters of the given values lie below a given score:

	>>> percentileofscore([1, 2, 3, 4], 3)
	75.0

	With multiple matches, note how the scores of the two matches, 0.6
	and 0.8 respectively, are averaged:

	>>> percentileofscore([1, 2, 3, 3, 4], 3)
	70.0

	Only 2/5 values are strictly less than 3:

	>>> percentileofscore([1, 2, 3, 3, 4], 3, kind='strict')
	40.0

	But 4/5 values are less than or equal to 3:

	>>> percentileofscore([1, 2, 3, 3, 4], 3, kind='weak')
	80.0

	The average between the weak and the strict scores is

	>>> percentileofscore([1, 2, 3, 3, 4], 3, kind='mean')
	60.0

	'''
	a = np.array(a)
	n = len(a)

	if kind == 'rank':
		if not(np.any(a == score)):
			a = np.append(a, score)
			a_len = np.array(range(len(a)))
		else:
			a_len = np.array(range(len(a))) + 1.0

		a = np.sort(a)
		idx = [a == score]
		pct = (np.mean(a_len[idx]) / n) * 100.0
		return pct

	elif kind == 'strict':
		return sum(a < score) / float(n) * 100
	elif kind == 'weak':
		return sum(a <= score) / float(n) * 100
	elif kind == 'mean':
		return (sum(a < score) + sum(a <= score)) * 50 / float(n)
	else:
		raise ValueError, "kind can only be 'rank', 'strict', 'weak' or 'mean'"