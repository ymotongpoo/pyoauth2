.. -*- coding: utf-8 -*-

pyoauth2: Simple OAuth 2.0 client
=================================

Release v\ |version|

:Author: `Yoshifumi YAMAGUCHI`_
:version: |version|
:Website: http://pyoauth2.rtfd.org
:PyPI: http://pypi.python.org/pypi/pyoauth2
:GitHub: https://github.com/ymotongpoo/pyoauth2
:License: New BSD License
:Issue Tracker: `Issues page on repository`_

.. _Yoshifumi YAMAGUCHI: https://plus.google.com/114892104481751903211/about
.. _Issues page on repository: https://github.com/ymotongpoo/pyoauth2/issues

pyoauth2 is a New BSD Licensed library, written in Python.

pyoauth2 provides simple `OAuth 2.0`_ client, which enables easy authorization to several web service APIs, such as Google APIs, Facebook API, Foursquare and so on. (Note that Twitter does not provide OAuth 2.0 as of now.)

This module tries to follow detailed specs on Internet-Draft of OAuth 2.0 (Candidate replacement of RFC 5849) but as of now it is implemented on a visceral level.   

.. _OAuth 2.0: http://tools.ietf.org/html/draft-ietf-oauth-v2

.. Warning::

   For the meantime, pyoauth2's target is command-line OAuth 2.0 client application, which means no redirects to callback and so forth.


Features
--------

pyoauth2 aims at offering user extensibility for following functions:

- Authorization flow
- Credential storage


User Guide
----------

This part of documentation explains background information about pyoauth2, step-by-step nutsshell and detailed API documents.

.. toctree::
   :maxdepth: 2

   user/introduction
   user/installation
   user/quickstart


API
---

.. toctree::
   :maxdepth: 1

   api/client.rst


Developer Guide
---------------

.. toctree::
   :maxdepth: 2

   development


