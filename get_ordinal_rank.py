def get_ordinal_rank(queryset, obj):
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
	index = list(queryset).index(obj)
	return index + 1