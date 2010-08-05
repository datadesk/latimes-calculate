from setuptools import setup, find_packages

setup(name='calculate',
      version='0.1',
      description='A collection of quickie math functions. Nothing too fancy.',
      author='Ben Welsh',
      author_email='Benjamin.Welsh@latimes.com',
      url='http://github.com/datadesk/latimes-calculate',
      download_url='http://github.com/datadesk/latimes-calculate.git',
      packages=find_packages(),
      license='MIT',
      keywords='math statistics gis geospatial numbers',
      classifiers=["Intended Audience :: Developers",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules"
                   ],
     )
