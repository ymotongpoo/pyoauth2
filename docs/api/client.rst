.. -*- coding: utf-8 -*-

API
===

Basics
------

.. module:: pyoauth2.client

.. class:: Storage()

   .. method:: get()

      Abstract implementation for getting credentials from actual storage.
      Inherited class must implement concretes for 

   .. method:: save()

      Abstract implementation for storing credentials into storage defined
      in inherited subclasses, such as file, database, on-memory and so on.


.. module:: pyoauth2.client

.. class:: FileStorage(filename)

   .. method:: get()

      Retrieve credentials from :ref:`filename` as python dictionary object

   .. method:: save(data)

      Save credential data into pre-defined file

