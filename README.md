XY
==

[![Build Status](https://travis-ci.org/jacebrowning/xy.png?branch=master)](https://travis-ci.org/jacebrowning/xy)
[![Coverage Status](https://coveralls.io/repos/jacebrowning/xy/badge.png?branch=master)](https://coveralls.io/r/jacebrowning/xy?branch=master)
[![PyPI Version](https://badge.fury.io/py/XY.png)](http://badge.fury.io/py/XY)

XY manages document and spreadsheet formats as text.



Getting Started
===============

Requirements
------------

* Python 3.3: http://www.python.org/download/releases/3.3.3/#download


Installation
------------

XY can be installed with ``pip``:

    pip install XY

Or directly from the source code:

    python setup.py install



Basic Usage
===========

After installation, abstract base classes can be imported from the package:

    python
    >>> import xy
    xy.__version__



For Contributors
================

Requirements
------------

* GNU Make:
    * Windows: http://cygwin.com/install.html
    * Mac: https://developer.apple.com/xcode
    * Linux: http://www.gnu.org/software/make (likely already installed)
* virtualenv: https://pypi.python.org/pypi/virtualenv#installation
* Pandoc: http://johnmacfarlane.net/pandoc/installing.html


Installation
------------

Create a virtualenv:

    make env

Run the tests:

    make test
    make tests  # includes integration tests

Build the documentation:

    make doc

Run static analysis:

    make pep8
    make pylint
    make check  # pep8 and pylint

Prepare a release:

    make dist  # dry run
    make upload
