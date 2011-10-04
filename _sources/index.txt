.. epigraph::

    A collection of simple math functions

Features
========

* Descriptive statistics like mean, median, percentile
* Comparison statistics like percentage change and per capita
* Ordinal, decile and competition rankings
* Geospatial stats like mean center and standard deviation distance
* A grabbag of utilities for a Dorling cartogram, diversity index, Benford's Law and generating random points

.. raw:: html

   <hr>

Getting started
===============

Install the latest package from pypi.

.. code-block:: bash

    $ pip install latimes-calculate

.. raw:: html

   <hr>

Functions
=========

.. method:: adjusted_monthly_value(value, datetime)

    Accepts a value and a datetime object, and then prorates the value to a 30-day figure depending on how many days are in the month.

    This can be useful for month-to-month comparisons in circumstances where fluctuations in the number of days per month may skew the analysis.

    For instance, February typically has only 28 days, in comparison to March, which has 31.

    .. code-block:: python

        >> import calculate
        >> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 4, 1))
        10.0
        >> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 2, 17))
        10.714285714285714
        >> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 12, 31))
        9.67741935483871


.. toctree::
   :maxdepth: 3
