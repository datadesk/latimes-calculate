.. epigraph::

    A collection of simple math functions

Features
========

* Descriptive statistics like mean, median, percentile
* Comparison statistics like percentage change, per-capita and rankings
* Geospatial stats like mean center and standard deviation distance
* A small dab of more complicated hoohah like Pearson's R.
* A grabbag of utilities for a Dorling cartogram, diversity index, Benford's Law, generating random points and other things

.. raw:: html

   <hr>

Dependencies
============

For more functions, nothing. `GeoDjango <http://www.google.com/search?client=ubuntu&channel=fs&q=geodjango&ie=utf-8&oe=utf-8>`_ is required for a small number of the geospatial functions, though the rest of the module will work if it is not installed.

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

    The function returns the Pearson correlation coefficient, also known as Pearson's r, which reports how closely the two datasets are related. This function also includes a variation on the classic Benford analysis popularized by blogger Nate Silver, who conducted an analysis of the final digits of polling data. To use Silver's variation, provide the keyword argument `method` with the value 'last_digit'. To prevent the function from printing, set the optional keyword argument `verbose` to False.

    This function is based upon code from a variety of sources around the web, but owes a particular debt to the work of Christian S. Perone. ::
        
        >>> import calculate
        >>> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        BENFORD'S LAW: FIRST_DIGIT
        
        Pearson's R: 0.86412304649
        
        | Number | Count | Expected Percentage | Actual Percentage |
        ------------------------------------------------------------
        | 1      | 2     | 30.1029995664       | 20.0              |
        | 2      | 1     | 17.6091259056       | 10.0              |
        | 3      | 1     | 12.4938736608       | 10.0              |
        | 4      | 1     | 9.69100130081       | 10.0              |
        | 5      | 1     | 7.91812460476       | 10.0              |
        | 6      | 1     | 6.69467896306       | 10.0              |
        | 7      | 1     | 5.79919469777       | 10.0              |
        | 8      | 1     | 5.11525224474       | 10.0              |
        | 9      | 1     | 4.57574905607       | 10.0              |
        
        >>> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], verbose=False)
        -0.863801937698704

.. method:: competition_rank(data_list, obj, order_by, direction='desc')

    Accepts a list, an item plus the value and direction to order by. Then returns the supplied object's competition rank as an integer. In competition ranking equal numbers receive the same ranking and a gap is left before the next value (i.e. "1224"). You can submit a Django queryset, objects, or just a list of dictionaries. ::

        >>> import calculate
        >>> qs = Player.objects.all().order_by("-career_home_runs")
        >>> ernie = Player.objects.get(first_name__iexact='Ernie', last_name__iexact='Banks')
        >>> eddie = Player.objects.get(first_name__iexact='Eddie', last_name__iexact='Matthews')
        >>> mel = Player.objects.get(first_name__iexact='Mel', last_name__iexact='Ott')
        >>> calculate.competition_rank(qs, ernie, career_home_runs', direction='desc')
        21
        >>> calculate.competition_rank(qs, eddie, 'career_home_runs', direction='desc')
        21
        >>> calculate.competition_rank(qs, mel, 'career_home_runs', direction='desc')
        23

.. method:: date_range(start_date, end_date)

    Returns a generator of all the days between two date objects. Results include the start and end dates. Arguments can be either datetime.datetime or date type objects.
    
    .. code-block:: python
        
        >>> import datetime
        >>> import calculate
        >>> dr = calculate.date_range(datetime.date(2009,1,1), datetime.date(2009,1,3))
        >>> dr
        <generator object at 0x718e90>
        >>> list(dr)
        [datetime.date(2009, 1, 1), datetime.date(2009, 1, 2), datetime.date(2009, 1, 3)]

.. method:: decile(data_list, score, kind='weak')

    Accepts a sample of values and a single number to add to it and determine the decile equivilent of its percentile rank.
    
    By default, the method used to negotiate gaps and ties is "weak" because it returns the percentile of all values
    at or below the provided value. For an explanation of alternative methods, refer to the ``percentile`` function. ::

        >>> import calculate
        >>> calculate.decile([1, 2, 3, 3, 4], 3)
        9

.. method:: elfi(data_list)

    The ELFI is a simplified method for calculating the Ethnolinguistic Fractionalization Index (ELFI). This is one form of what is commonly called a "diversity index." Accepts a list of decimal percentages, which are used to calculate the index. Returns a decimal value as a floating point number. ::

        >>> import calculate
        >>> calculate.elfi([0.2, 0.5, 0.05, 0.25])
        0.64500000000000002

.. method:: mean(data_list)

    Accepts a sample of values and returns their mean. The mean is the sum of all values in the sample divided by the number of members. It is also known as the average. Since the value is strongly influenced by outliers, median is generally a better indicator of central tendency. ::

        >>> import calculate
        >>> calculate.mean([1,2,3])
        2.0
        >>> calculate.mean([1, 99])
        50.0

.. method:: mean_center(obj_list, point_attribute_name='point')

    Accepts a geoqueryset, list of objects or list of dictionaries, expected to contain `GeoDjango Point <https://docs.djangoproject.com/en/dev/ref/contrib/gis/geos/#point>`_ objects as one of their attributes. Returns a Point object with the mean center of the provided points. The mean center is the average x and y of all those points. By default, the function expects the Point field on your model to be called 'point'. If the point field is called something else, change the kwarg 'point_attribute_name' to whatever your field might be called. ::

        >>> import calculate
        >>> calculate.mean_center(qs)
        <Point object at 0x77a1694>

.. method:: median(data_list)

    Accepts a list of numbers and returns the median value. The median is the number in the middle of a sequence, with 50 percent of the values above, and 50 percent below. In cases where the sequence contains an even number of values -- and therefore no exact middle -- the two values nearest the middle are averaged and the mean returned. ::

        >>> import calculate
        >>> calculate.median([1,2,3])
        2.0
        >> calculate.median((1,4,3,2))
        2.5

.. method:: mode(data_list)

    Accepts a sample of numbers and returns the mode value. The mode is the most common value in a data set. If there is a tie for the highest count, no value is returned. ::

        >>> import calculate
        >>> calculate.mode([1,2,2,3])
        2.0
        >>> calculate.mode([1,2,3])
        >>> 

.. method:: nudge_points(geoqueryset, point_attribute_name='point', radius=0.0001)

    A utility that accepts a GeoDjango QuerySet and nudges slightly apart any identical points. Nothing is returned. By default, the distance of the move is 0.0001 decimal degrees. I'm not sure if this will go wrong if your data is in a different unit of measurement. This can be useful for running certain geospatial statistics, or even for presentation issues, like spacing out markers on a Google Map for instance. ::

        >>> import calculate
        >>> calculate.nudge_points(qs)
        >>>

.. method:: ordinal_rank(sequence, item, order_by=None, direction='desc')

    Accepts a list and an object. Returns the object's ordinal rank as an integer. Does not negiotiate ties. ::

        >>> import calculate
        >>> qs = Player.objects.all().order_by("-career_home_runs")
        >>> barry = Player.objects.get(first_name__iexact='Barry', last_name__iexact='Bonds')
        >>> calculate.ordinal_rank(qs, barry)
        1

.. method:: pearson(list_one, list_two)

    Accepts paired lists and returns a number between -1 and 1, known as `Pearson's r <http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient>`_, that indicates of how closely correlated the two datasets are. A score of close to one indicates a high positive correlation. That means that X tends to be big when Y is big. A score close to negative one indicates a high negative correlation. That means X tends to be small when Y is big. A score close to zero indicates little correlation between the two datasets.

    A warning, though, correlation does not equal causation. Just because the two datasets are closely related doesn't not mean that one causes the other to be the way it is. ::

        >>> import calculate
        >>> calculate.pearson([6,5,2], [2,5,6])
        -0.8461538461538467

.. method:: per_capita(value, population, per=10000, fail_silently=True)

    Accepts two numbers, a value and population total, and returns the per capita rate. By default, the result is returned as a per 10,000 person figure. If you divide into zero -- an illegal operation -- a null value is returned by default. If you prefer for an error to be raised, set the kwarg 'fail_silently' to False. ::

        >>> import calculate
        >>> calculate.per_capita(12, 100000)
        1.2

.. method:: per_sqmi(value, square_miles, fail_silently=True)

    Accepts two numbers, a value and an area, and returns the per square mile rate. Not much more going on here than a simple bit of division. If you divide into zero -- an illegal operation -- a null value is returned by default. If you prefer for an error to be raised, set the kwarg 'fail_silently' to False. ::

        >>> import calculate
        >>> calculate.per_sqmi(20, 10)
        2.0




