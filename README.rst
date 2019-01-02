
pyVigicrues
=======

.. image:: https://travis-ci.org/Mickaelh51/pyVigicrues.svg?branch=master
    :target: https://travis-ci.org/Mickaelh51/pyVigicrues

.. image:: https://img.shields.io/pypi/v/pyVigicrues.svg
    :target: https://pypi.python.org/pypi/pyVigicrues

.. image:: https://img.shields.io/pypi/pyversions/pyVigicrues.svg
    :target: https://pypi.python.org/pypi/pyVigicrues

.. image:: https://requires.io/github/Mickaelh51/pyVigicrues/requirements.svg?branch=master
    :target: https://requires.io/github/Mickaelh51/pyVigicrues/requirements/?branch=master
    :alt: Requirements Status

Get level and speed from many French rivers (https://www.vigicrues.gouv.fr/)

Installation
------------

The easiest way to install the library is using `pip <https://pip.pypa.io/en/stable/>`_::

    pip install pyvigicrues

You can also download the source code and install it manually::

    cd /path/to/pyvigicrues/
    python setup.py install

Usage
-----
Print your current data

    pyvigicrues -s <STATIONID> -t <TYPE OF DATA>

- Ex: pyvigicrues -s H523102501 -t H # for level
- Ex: pyvigicrues -s H523102501 -t Q # for speed

Dev env
-------
create virtual env and install requirements

    virtualenv -p /usr/bin/python3.5 env
    pip install -r requirements.txt
