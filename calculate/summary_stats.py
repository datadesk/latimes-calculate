import calculate

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
    
    print """
Summary statistics
==================

n:        %s
max:        %s
min:        %s
range:        %s
mean:        %s
median:        %s
mode:        %s
std:        %s
""" % (n, max_, min_, range_, mean, median, mode, standard_deviation)
