.. -*- coding: utf-8; mode: rst -*-

Welcome to pyoauth2
===================

0. What is pyoauth2 about?
--------------------------

pyoauth2 provides simple `OAuth 2.0`_ client, which enables 
easy authorization/authentication to several web service APIs, such as
Google APIs, Facebook API, Foursquare and so on.
(Note that Twitter does not provide OAuth 2.0 as of now.)

This module tries to follow detailed specs on Internet-Draft of OAuth 2.0
(Candidate replacement of RFC 5849) but as of now it is implemented on a
visceral level.

.. _OAuth 2.0: http://tools.ietf.org/html/draft-ietf-oauth-v2


1. Lisence
----------

pyoauth2 is distributed under New BSD Lisence.
See LISENCE file for details.


2. Requirements
---------------

pyoauth2 depends on following modules:

- `requests`_


Actually urllib2 can handle same functions as requests but
in order to realize more simple and readable code, requests
module was selected for HTTP transaction.

.. _requests: http://pypi.python.org/pypi/requests


3. Installation
---------------

pyoauth2 is registered on PyPI so you can install this library
with pip and easy_install if you are connected to the internet.

.. ::

   $ pip install pyoauth2


Otherwise, you can run setup.py in Python 2.7 or setup.cfg in Python 3.3+
for installing pyoauth2

.. ::

   $ python setup.py install


4. Getting Started
------------------

for detailed document, see http://readthedocs.org/docs/pyoauth2/


5. Changelog
------------

* 2012-04-27    version 0.0.4 released

  * started Python 3 support

* 2012-04-24    version 0.0.3 released
  
  * enabled server side usage

* 2012-04-23    version 0.0.2 released

  * fixed sample

* 2012-04-20    version 0.0.1 released

  * first release
