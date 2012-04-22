.. -*- coding: utf-8 -*-

.. _installation:

Installation
============

This part of documentation describes installation of pyoauth2.


pip & easy_install
------------------

Python has several package management tools, and the most famous ones are `pip`_ and `easy_install`_. Of course pyoauth2 can be installed with these tools.
You can simply run following command on your console.

.. code-block:: bash

   $ pip install pyoauth2

or

.. code-block:: bash

   $ easy_install pyoauth2

.. _pip: http://pypi.python.org/pypi/pip
.. _easy_install: http://pypi.python.org/pypi/setuptools


From the code
-------------

pyoauth2 is developed on GitHub and `the code`_ is always open to everyone.

You can install pyoauth2 from the latest source code with pip or setup.py

In the case of pip, you can specify target URL to the GitHub repository with ``-e`` option:

.. code-block:: bash

   $ pip install -e git+https://ymotongpoo@github.com/ymotongpoo/pyoauth2.git#egg=pyoauth2

Otherwise, simply download source code in zip archive or fetch repository using Git, and run :file:`setup.py` script.

.. code-block:: bash

   $ curl -OL "https://github.com/ymotongpoo/pyoauth2/zipball/master" -o pyoauth2.zip
   $ unzip pyoauth2.zip
   $ cd pyoauth2
   $ python setup.py install

.. _the code: https://github.com/ymotongpoo/pyoauth2

