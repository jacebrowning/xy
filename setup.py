#!/usr/bin/env python

"""
Setup script for XY.
"""

import setuptools

from xy import __project__, CLI

# Touch the README, it will be generated on release (`make doc`)
README = 'README.rst'
import os
if not os.path.exists(README):
    open(README, 'w').close()
CHANGES = 'CHANGES.md'


setuptools.setup(
    name=__project__,
    version='0.0.0',

    description="XY manages document and spreadsheet formats as text.",
    url='http://github.com/jacebrowning/xy',
    author='Jace Browning',
    author_email='jacebrowning@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [CLI + ' = xy.cli:main']},

    long_description=(open(README).read() + '\n' +
                      open(CHANGES).read()),
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=[],
)
