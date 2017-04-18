.. _curl:

****
Curl
****

In this page you will find documentation about how to access SWIFT through curl.

.. contents:: 
    :depth: 4

=====
Usage
=====

Here we refer to the man pages of **curl**.

==============
Authentication
==============


First you need to get a token that is valid for 24 hours that can be used instead of user name  and password. This goes as follows:

.. code-block:: console

    curl -i -H "X-Auth-User: <user name>" -H "X-Auth-Key: <password>" https://proxy.swift.surfsara.nl/auth/v1.0
       .
       .
    X-Storage-Url: https://proxy.swift.surfsara.nl/v1/AUTH_ron
    X-Auth-Token: <token>
       .
       .

Here **X-Auth-Token** is the token and **X-Storage-Url** is the storage URL that you will need later on.

Now you can run curl commands using:

.. code-block:: console

    curl -i -H "X-Auth-Token: <token>" ...

==================
Create a container
==================

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: <token>" <storage url>/mycontainer

===============================
Upload an object to a container
===============================

.. code-block:: console

    curl -i -T myobject -X PUT -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

