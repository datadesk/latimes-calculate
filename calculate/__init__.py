from age import age
from adjusted_monthly_value import adjusted_monthly_value
from at_percentile import at_percentile
from benfords_law import benfords_law
from competition_rank import competition_rank
from date_range import date_range
from decile import decile
from elfi import elfi
from margin_of_victory import margin_of_victory
from mean import mean
from median import median
from mode import mode
from ordinal_rank import ordinal_rank
from pearson import pearson
from per_capita import per_capita
from per_sqmi import per_sqmi
from percentage_change import percentage_change
from percentage import percentage
from percentile import percentile
from range import range
from standard_deviation import standard_deviation
from summary_stats import summary_stats

# Test whether Django is installed
try:
    from django.conf import settings
    if settings.configured:
        HAS_DJANGO = True
        if 'django.contrib.gis' in settings.INSTALLED_APPS:
            HAS_GEODJANGO = True
        else:
            HAS_GEODJANGO = False
    else:
        HAS_DJANGO, HAS_GEODJANGO = False, False
except ImportError:
    HAS_DJANGO, HAS_GEODJANGO = False, False

# If it is, import all the functions that, at least for now, require GeoDjango
if HAS_DJANGO and HAS_GEODJANGO:
    from random_point import random_point
    from mean_center import mean_center
    from nudge_points import nudge_points
    from standard_deviation_distance import standard_deviation_distance
    from standard_deviation_ellipses import standard_deviation_ellipses
    from dorling_cartogram import dorling_cartogram
