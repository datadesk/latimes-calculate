.. epigraph::

    A collection of simple math functions

Features
========

* Descriptive statistics like mean, median, percentile
* Comparison statistics like percentage change and per capita
* Ordinal, decile and competition rankings
* Geospatial stats like mean center and standard deviation distance
* A small dab of more complicated hoohah like Pearson's R.
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
        
        >>> import calculate
        >>> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 4, 1))
        10.0
        >>> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 2, 17))
        10.714285714285714
        >>> calculate.adjusted_monthly_value(10, datetime.datetime(2009, 12, 31))
        9.67741935483871

.. method:: benfords_law(number_list, method='first_digit', verbose=True)

    Accepts a list of numbers and applies a quick-and-dirty run against Benford's Law. 

    Benford's Law makes statements about the occurance of leading digits in a dataset. It claims that a leading digit of 1 will occur about 30 percent of the time, and each number after it a little bit less, with the number 9 occuring the least. Datasets that greatly vary from the law are sometimes suspected of fraud.

    The function returns the Pearson correlation coefficient, also known as Pearson's r, which reports how closely the two datasets are related. This function also includes a variation on the classic Benford analysis popularized by blogger Nate Silver, who conducted an analysis of the final digits of polling data. To use Silver's variation, provide the keyward argument `method` with the value 'last_digit'. To prevent the function from printing, set the optional keyword argument `verbose` to False.

    This function is based upon code from a variety of sources around the web, but owes a particular debt to the work of Christian S. Perone. ::
        
        >>> import calculate
        >>> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        BENFORD'S LAW: FIRST_DIGIT
        
        Pearson's R: 0.86412304649
        
        | Number | Count | Expected Percentage | Actual Percentage |
        ------------------------------------------------------------
        | 1 | 2 | 30.1029995664 | 20.0 |
        | 2 | 1 | 17.6091259056 | 10.0 |
        | 3 | 1 | 12.4938736608 | 10.0 |
        | 4 | 1 | 9.69100130081 | 10.0 |
        | 5 | 1 | 7.91812460476 | 10.0 |
        | 6 | 1 | 6.69467896306 | 10.0 |
        | 7 | 1 | 5.79919469777 | 10.0 |
        | 8 | 1 | 5.11525224474 | 10.0 |
        | 9 | 1 | 4.57574905607 | 10.0 |
        
        >>> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], verbose=False)
        -0.863801937698704

.. toctree::
   :maxdepth: 3
