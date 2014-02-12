XY
==

[![Build Status](https://travis-ci.org/jacebrowning/xy.png?branch=master)](https://travis-ci.org/jacebrowning/xy)
[![Coverage Status](https://coveralls.io/repos/jacebrowning/xy/badge.png?branch=master)](https://coveralls.io/r/jacebrowning/xy?branch=master)
[![PyPI Version](https://badge.fury.io/py/XY.png)](http://badge.fury.io/py/XY)

XY manages document and spreadsheet formats as text.

[![x all the y](http://static.starcitygames.com/www/images/article/02082012levin.png)](http://hyperboleandahalf.blogspot.com/2010/06/this-is-why-ill-never-be-adult.html)

What?
-----

XY is a convention and tool for storing document and spreadsheet data in text files while maintaining support for editing in traditional `.docx` and `.xlsx` programs.


Why?
----

Text files are great because they be stored in verson control and diffed/branched/merged/etc. But sometimes there is a need or precident for supporting traditional document and spreadsheet formats. Unfortunately, these formats **do not** play nice with version control. That's where XY comes in.


How?
----

Create a new document or spreadsheet:

    $ xy MyDocument.docxy
    $ xy MySpreadsheet.xlsxy

Or convert an exsting file to the XY format:

    $ xy --convert MyDocument.docx
    $ xy --convert MySpreadsheet.xlsx

When editing, the file will be opened using the associated `.docx` or `.xlsx` editor:

    $ xy MyFile.docxy



Getting Started
===============


Requirements
------------

* Python 3.3: http://www.python.org/download/releases/3.3.4/#download
* an `.xlsx` or `.docx` editor


Installation
------------

XY can be installed with ``pip``:

    pip install XY

Or directly from the source code:

    python setup.py install



Basic Usage
===========

After installation, use the command-line interface:

    $ xy --help



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
