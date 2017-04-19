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

Here we refer to the man pages of **curl**. But we do like to point out the following options:

:manpage:`curl(1)`

-i	Include the HTTP-header in the output. The HTTP-header includes things like server-name, date of the document, HTTP-version  and more...
-s	Silent or quiet mode. Don't show progress meter  or  error  messages.   Makes  curl mute. It will still output the data you ask for, potentially even to the terminal/stdout unless you redirect it.
-S	When used with -s, it makes curl show an error message if it fails.


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


================
Getting metadata
================

Information about containers can be obtained by:

.. code-block:: console

    curl -i --head -H "X-Auth-Token: <token>" <storage url>/mycontainer


Information about an object can be retrieved through:

.. code-block:: console

    curl -i --head -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

================================
List the container of an account
================================

.. code-block:: console

    curl -s -S -X GET -H "X-Auth-Token: <token>" <storage url>

================================
List the contents of a container
================================

.. code-block:: console

    curl -s -S -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer

==================
Delete a container
==================

.. code-block:: console

    curl -s -S -X DELETE -H "X-Auth-Token: <token>" <storage url>/mycontainer

.. note:: **Important:** You can only delete an empty container. If you try to delete a non empty container, then you get the error message: "There was a conflict when trying to complete your request."

================
Delete an object
================

.. code-block:: console

    curl -s -S -X DELETE -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

========================================================
Set and get your own metadata for containers and objects
========================================================

For containers we have:

.. code-block:: console

    curl -s -S -X POST -H "X-Auth-Token: <token>" -H "X-Container-Meta-mymetadata: mystuff" <storage url>/mycontainer

.. note:: **Important:** The header which denotes the metadata item has to be of the form *X-Container-Meta-<name>* for containers.

For objects we have:

.. code-block:: console

    curl -s -S -X POST -H "X-Auth-Token: <token>" -H "X-Object-Meta-mymetadata: mystuff" <storage url>/mycontainer/myobject

.. note:: **Important:** The header which denotes the metadata item has to be of the form *X-Object-Meta-<name>* for objects.

Get the metadata for containers:

.. code-block:: console

    curl -s -S --head -H "X-Auth-Token: <token>" <storage url>/mycontainer

which lists only the metadata. Or:

.. code-block:: console

    curl -i -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer

which shows container metadata and lists objects. 

Get the metadata for objects:

.. code-block:: console

    curl -s -S --head -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

which lists only the metadata. Or:

.. code-block:: console

    curl -i -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

which shows container metadata and gets the object data.

============================
Uploading large files (>5GB)
============================

It is only possible to upload objects with the size of at most 5GB in one go to SWIFT. It is possible to up and download larger objects. For this we refer to the documentation on large objects at: https://docs.openstack.org/developer/swift/overview_large_objects.html

===============
Bulk operations
===============

You can upload a tarball which will be extracted by SWIFT.

.. image /Images/bulk_upload.png

It is possible to do a bulk deletion. First you create a text file with all the containers and objects to be deleted. After that everything goes as follows:

.. image /Images/bulk_deletion.png

=================
Object versioning
=================
TBD
