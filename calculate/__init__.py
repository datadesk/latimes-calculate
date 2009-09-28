from adjusted_monthly_value import adjusted_monthly_value
from benfords_law import benfords_law
from date_range import date_range
from decile import decile
from elfi import elfi
from mean import mean
from median import median
from mode import mode
from per_capita import per_capita
from per_sqmi import per_sqmi
from percentage_change import percentage_change
from percentage import percentage
from percentile import percentile
from random_point import random_point
from range import range
from standard_deviation import standard_deviation
from summary_stats import summary_stats

# Test whether Django is installed
from django.conf import settings
if settings.configured:
	HAS_DJANGO = True
else:
	HAS_DJANGO = False

# If it is, import all the functions that, at least for now, require Django
if HAS_DJANGO:
	from ordinal_rank import ordinal_rank
	from competition_rank import competition_rank
	from random_point import random_point
	from mean_center import mean_center
	from nudge_points import nudge_points
	from standard_deviation_distance import standard_deviation_distance
	from standard_deviation_ellipses import standard_deviation_ellipses
