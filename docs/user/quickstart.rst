.. -*- coding: utf-8 -*-

Quickstart
==========

Are you ready to start your application? This guide shows a small introduction about how to get started with pyoauth2. Before reading contents below, please make sure that you have already gone througth the previous section :ref:`Installation`.

Create a credential storage
---------------------------

Before starting OAuth 2.0 authorization process, a credential storage instance should be created for storing OAuth 2.0 related credential information such as access token, expire date and so on. pyoauth2 expects 1 storage for 1 client.

.. code-block:: python

   storage = FileStorage('test.dat')

To get credentials stored in the storage instance, you can use ``get()`` method and for saving newly fetched or updated existing credentials you can use ``save()`` method.

.. code-block:: python

   credentials = storage.get()
   ...
   do_some_process(credentials)
   ...
   storage.save(credentials)


Prepare OAuth 2.0 flow instance
-------------------------------

Flow instance is the basic object for following OAuth 2.0 procedure.

.. code-block:: python

   flow = OAuth2AuthorizationFlow(required_params,
                                  extra_auth_params=extra_auth_params,
                                  extra_token_params=extra_token_params,
                                  local=True)

   flow.retrieve_authorization_code()
   credentials = flow.retrieve_token()
   

Variables for ``required_params``, ``extra_auth_params``, ``extra_token_params`` are dictionary which contains parameters for requests to the OAuth 2.0 server such as "Client id", "Client secret", "Redirect URI" and so on. See a complete example for keys and values for them.


Example code
------------

Basically, only 2 objects above are required for authorization. Following code is a small but simple sample code for communicating with YouTube API.

.. literalinclude:: ../../samples/youtube.py

