from __future__ import print_function
import calculate
from calculate import ptable


def summary_stats(data_list):
    """
    Accepts a sample of numbers and returns a pretty
    print out of a variety of descriptive statistics.
    """
    mean = calculate.mean(data_list)
    median = calculate.median(data_list)
    mode = calculate.mode(data_list)
    n = len(data_list)
    max_ = max(data_list)
    min_ = min(data_list)
    range_ = calculate.range(data_list)
    standard_deviation = calculate.standard_deviation(data_list)
    variation_coefficient = calculate.variation_coefficient(data_list)

    table = ptable.indent(
        [
            ['Statistic', 'Value'],
            ['n', str(n)],
            ['mean', str(mean)],
            ['median', str(median)],
            ['mode', str(mode)],
            ['maximum', str(max_)],
            ['minimum', str(min_)],
            ['range', str(range_)],
            ['standard deviation', str(standard_deviation)],
            ['variation coefficient', str(variation_coefficient)],
        ],
        hasHeader=True,
        separateRows=False,
        prefix="| ", postfix=" |",
    )
    print(table)
