<pre><code> dP""b8    db    88      dP""b8 88   88 88        db    888888 888888 
dP   `"   dPYb   88     dP   `" 88   88 88       dPYb     88   88__   
Yb       dP__Yb  88  .o Yb      Y8   8P 88  .o  dP__Yb    88   88""   
 YboodP dP""""Yb 88ood8  YboodP `YbodP' 88ood8 dP""""Yb   88   888888</code></pre>

Some simple math we use to do journalism.

[![Build Status](https://travis-ci.org/datadesk/latimes-calculate.png?branch=master)](https://travis-ci.org/datadesk/latimes-calculate)
[![PyPI version](https://badge.fury.io/py/latimes-calculate.png)](http://badge.fury.io/py/latimes-calculate)
[![Coverage Status](https://coveralls.io/repos/datadesk/latimes-calculate/badge.png?branch=master)](https://coveralls.io/r/datadesk/latimes-calculate?branch=master)

* Documentation: [http://datadesk.github.io/latimes-calculate/](http://datadesk.github.io/latimes-calculate/)
* Issues: [https://github.com/datadesk/latimes-calculate/issues](https://github.com/datadesk/latimes-calculate/issues)
* Packaging: [https://pypi.python.org/pypi/latimes-calculate](https://pypi.python.org/pypi/latimes-calculate)
* Testing: [https://travis-ci.org/datadesk/latimes-calculate](https://travis-ci.org/datadesk/latimes-calculate)
* Coverage: [https://coveralls.io/r/datadesk/latimes-calculate](https://coveralls.io/r/datadesk/latimes-calculate)

Features
--------

* Descriptive statistics like mean, median, percentile
* Comparison statistics like percentage change, per-capita and rankings
* Geospatial stats like mean center and standard deviation distance
* A small dab of more complicated hoohah like Pearson’s R.
* A grabbag of utilities for a diversity index, Benford’s Law, generating random points and other things

Dependencies
------------

For most functions, nothing. "GeoDjango":http://www.geodjango.org/ is required for a small number of the geospatial functions, though the rest of the module will work if it is not installed.

Getting started
---------------

Install from PyPI

```bash
$ pip install latimes-calculate
```

Experiment in Python shell

```python
>>> import calculate
>>> calculate.percentage_change(100, 150)
50.0
```
