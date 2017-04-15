.. _python-swift-client:

*******************
Python SWIFT client
*******************

In this page you will find documentation about the Python SWIFT client that are available.

.. contents:: 
    :depth: 4

=============
Authorisation
=============

.. image:: /Images/auth.jpg
           :width: 300px
           :height: 225px

The following environment variables are useful to set if you don't want them to provide them all the time on the command line.

.. code-block:: console

         export ST_AUTH=https://proxy.swift.surfsara.nl/auth/v1.0
         export ST_USER=<my user name>
         export ST_KEY=<my password>

==================
Create a container
==================

.. image:: /Images/make_container.png
           :width: 316px


A container can be created by the following command:

.. code-block:: console

         swift post mycontainer

===============================
Upload an object to a container
===============================

.. image:: /Images/upload.jpg
           :width: 300px


.. code-block:: console

         swift upload mycontainer myobject

If the container **mycontainer** does not exist yet, then it will be created.

================
Getting metadata
================

.. image:: /Images/metadata.jpg
           :width: 600px

Container metadata can be obtained in the following manner:

.. image:: /Images/stat_container.png
           :width: 600px

Bytes is the total number of bytes of all object in the container
Objects is the number of objects in the container
X-Storage-Policy is the storage policy

Object metadata can be obtained by the following command:

.. image:: /Images/stat_object.png
           :width: 600px

Content Length is the size in bytes.
ETag is the md5 checksum of the object



.. Links:

.. _`SURFsara helpdesk`: https://www.surf.nl/en/about-surf/contact/helpdesk-surfsara-services/index.html

.. _`SURFsara application form`: https://e-infra.surfsara.nl/
