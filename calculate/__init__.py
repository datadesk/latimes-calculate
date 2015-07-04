from __future__ import absolute_import
from .age import age
from .adjusted_monthly_value import adjusted_monthly_value
from .at_percentile import at_percentile
from .benfords_law import benfords_law
from .competition_rank import competition_rank
from .date_range import date_range
from .decile import decile
from .elfi import elfi
from .equal_sized_breakpoints import equal_sized_breakpoints
from .margin_of_victory import margin_of_victory
from .mean import mean
from .median import median
from .mode import mode
from .ordinal_rank import ordinal_rank
from .pearson import pearson
from .per_capita import per_capita
from .per_sqmi import per_sqmi
from .percentage_change import percentage_change
from .percentage import percentage
from .percentile import percentile
from .range import range
from .split_at_breakpoints import split_at_breakpoints
from .standard_deviation import standard_deviation
from .summary_stats import summary_stats
from .variation_coefficient import variation_coefficient

DJANGO_MODULES = [
    'age',
    'adjusted_monthly_value',
    'at_percentile',
    'benfords_law',
    'competition_rank',
    'date_range',
    'decile',
    'elfi',
    'equal_sized_breakpoints',
    'margin_of_victory',
    'mean',
    'median',
    'mode',
    'ordinal_rank',
    'pearson',
    'per_capita',
    'per_sqmi',
    'percentage_change',
    'percentage',
    'percentile',
    'range',
    'split_at_breakpoints',
    'standard_deviation',
    'summary_stats',
    'variation_coefficient',
]
__all__ = DJANGO_MODULES

# Test whether Django is installed
try:
    import django
    assert django
    HAS_DJANGO = True
    from django.conf import settings
    if not settings.configured:
        settings.configure(DEBUG=True, TEMPLATE_DEBUG=True, TEMPLATE_DIRS=())
    try:
        from django.contrib.gis.geos.libgeos import geos_version
        from django.contrib.gis.geos.libgeos import geos_version_info
        assert geos_version
        assert geos_version_info
        HAS_GEODJANGO = True
    except ImportError:
        HAS_GEODJANGO = False
except ImportError:
    HAS_DJANGO, HAS_GEODJANGO = False, False

# If it is, import all the functions that, at least for now, require GeoDjango
if HAS_DJANGO and HAS_GEODJANGO:
    __all__ = [
        'age',
        'adjusted_monthly_value',
        'at_percentile',
        'benfords_law',
        'competition_rank',
        'date_range',
        'decile',
        'elfi',
        'equal_sized_breakpoints',
        'margin_of_victory',
        'mean',
        'median',
        'mode',
        'ordinal_rank',
        'pearson',
        'per_capita',
        'per_sqmi',
        'percentage_change',
        'percentage',
        'percentile',
        'range',
        'split_at_breakpoints',
        'standard_deviation',
        'summary_stats',
        'random_point',
        'mean_center',
        'nudge_points',
        'standard_deviation_distance',
        'variation_coefficient',
    ]
    from .random_point import random_point
    from .mean_center import mean_center
    from .nudge_points import nudge_points
    from .standard_deviation_distance import standard_deviation_distance
