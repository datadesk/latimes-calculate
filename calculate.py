import math
from scipy.stats import percentileofscore
from django.db.models.query import QuerySet

def decile(array, score, kind='weak'):
	"""
	Accepts an array of values and a singleton score.
	
	The score is run against the array to determine its percentile score.

	The value is then translated into a decile grouping and returned as an integer.
	
	By default, the percentile method used is weak. Others are detailed in the documentation below.
	
	h3. Example usage
	
		>>> get_decile([1, 2, 3, 3, 4], 3)
		9
	
	h3. Dependencies
	
	* "scipy":http://www.scipy.org/SciPy
	
	h3. Documentation
	
	* "scipy.stats.percentileofscore":http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.percentileofscore.html#scipy.stats.percentileofscore
	* "percentile rank":http://en.wikipedia.org/wiki/Percentile_rank
	* "decile":http://en.wikipedia.org/wiki/Decile
	
	"""
	if not isinstance(array, list):
		raise TypeError('first value input must be a list')
	percentile = percentileofscore(array, score, kind=kind)
	if percentile == 100.0:
		return 10
	else:
		decile = int(percentile * 0.1) + 1
		return decile
		

def elfi(array):
	"""
	Accepts a list of decimal percentages, which are used 
	to calculate the Ethnolinguistic Fractionalization Index (ELFI).
	
	The list must add up to one.

	The ELFI is a simplified method for calculating the 
	Ethnic Diversity Index. 
	
	Returns a decimal value as a floating point number.
	
	h3. Example usage
	
		>> get_elfi([0.2, 0.5, 0.05, 0.25])
		0.64500000000000002

	h3. Dependencies
	
		* "math":http://docs.python.org/library/math.html
	
	h3. Documentation
	
		* "ethnic diversity index":http://www.ed-data.k12.ca.us/articles/EDITechnical.asp
	
	"""
	if not isinstance(array, list):
		raise TypeError('input must be a list')
	if sum(array) != 1.0:
		raise ValueError('values of submitted array must add up to one. your list adds up to %s' % sum(array))
	elfi = 1 - sum([math.pow(i, 2) for i in array])
	return elfi


def ordinal_rank(queryset, obj):
	"""
	Accepts a Django queryset and Django object and
	returns the object's ordinal rank as an integer.
	
	h3. Example usage
	
		>> qs = Player.objects.all().order_by("-career_home_runs")
		>> barry = Player.objects.get(first_name__iexact='Barry', last_name__iexact='Bonds')
		>> get_ordinal_rank(qs, barry)
		1
	
	h3. Dependencies
	
		* "django":http://www.djangoproject.com/
	
	h3. Documentation
	
		* "ordinal rank":http://en.wikipedia.org/wiki/Ranking#Ordinal_ranking_.28.221234.22_ranking.29
	
	"""
	if not isinstance(queryset, QuerySet):
		raise TypeError('First parameter must be a Django QuerySet. You submitted a %s object' % type(queryset))
	index = list(queryset).index(obj)
	return index + 1

def per_capita(value, population, per=10000):
	try:
		rate = (float(value) / population) * per
		return rate
	except ZeroDivisionError:
		return None

def per_sqmi(value, square_miles):
	try:
		rate = float(value) / square_miles
		return rate
	except ZeroDivisionError:
		return None

def percent_change(old, new):
	change = new - old
	try:
		percent_change = (change / float(old))*100
		return percent_change
	except ZeroDivisionError:
		return None

def percentage(value, total):
	"""
	Accepts two integers, a value and a total. 
	
	The value is divided into the total and then multiplied by 100, 
	returning its percentage as a float.
	
	If one of the numbers is zero, a null value is returned.
	
	h3. Example usage
	
		>> get_percentage(2, 10)
		20.0
		
	h3. Documentation
	
		* "percentage":http://en.wikipedia.org/wiki/Percentage
	
	"""
	try:
		percent = (value / float(total))*100
		return percent
	except ZeroDivisionError:
		return None