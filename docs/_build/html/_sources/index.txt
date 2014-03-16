=================
latimes-calculate
=================

Some simple math we use to do journalism

Features
========

* Descriptive statistics like mean, median, percentile, mode, range, standard deviation
* Comparison statistics like percentage change, per-capita, per square mile, percentiles, deciles and rankings
* Geospatial stats like mean center and standard deviation distance
* A small dab of more complicated hoohah like Pearson's R.
* A grabbag of utilities for a diversity index, Benford’s Law, ages, margin of victory, date rates, making break points, generating random points and other things

Getting started
===============

Install the latest package from pypi.

.. code-block:: bash

    $ pip install latimes-calculate

.. note::

    For most functions, there are no additional requirements. The exception is
    the small number of geospatial functions, which require `GeoDjango <http://geodjango.org/>`_.

Documentation
-------------

.. toctree::
   :maxdepth: 2

   functions
   geospatialfunctions

Contributing
------------

* Code repository: `https://github.com/datadesk/latimes-calculate <https://github.com/datadesk/latimes-calculate>`_
* Issues: `https://github.com/datadesk/latimes-calculate/issues <https://github.com/datadesk/latimes-calculate/issues>`_
* Packaging: `https://pypi.python.org/pypi/latimes-calculate <https://pypi.python.org/pypi/latimes-calculate>`_
* Testing: `https://travis-ci.org/datadesk/latimes-calculate <https://travis-ci.org/datadesk/latimes-calculate>`_
* Coverage: `https://coveralls.io/r/datadesk/latimes-calculate <https://coveralls.io/r/datadesk/latimes-calculate>`_
