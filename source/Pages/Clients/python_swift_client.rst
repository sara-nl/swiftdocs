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
           :width: 600px

The following environment variables are useful to set if you don't want them to provide them all the time on the command line.

.. code-block:: console

         export ST_AUTH=https://proxy.swift.surfsara.nl/auth/v1.0
         export ST_USER=<my user name>
         export ST_KEY=<my password>

==================
Create a container
==================

.. image:: /Images/make_container.png
           :width: 600px


A container can be created by the following command:

.. code-block:: console

         swift post mycontainer

===============================
Upload an object to a container
===============================

.. image:: /Images/upload.jpg
           :width: 600px


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

**Bytes** is the total number of bytes of all object in the container, 
**Objects** is the number of objects in the container and 
**X-Storage-Policy** is the storage policy.

Object metadata can be obtained by the following command:

.. image:: /Images/stat_object.png
           :width: 600px

**Content Length** is the size in bytes and 
**ETag** is the md5 checksum of the object.

============================
List contents of a container
============================

.. image:: /Images/contents-container.jpg
           :width: 600px

The objects in a container can be listed like:

.. code-block:: console

         swift list mycontainer

====================================
Throwing containers and objects away
====================================

.. image:: /Images/delete_container.png

Delete one object from a container:

.. code-block:: console

         swift delete mycontainer myobject


Delete a container with all objects in it:

.. code-block:: console

         swift delete mycontainer

=======================================================
Script to verify MD5 checksums of local and remote copy
=======================================================

.. code-block:: console

    #!/bin/sh

    container=$1
    shift
    object=$1

    ETag=`swift stat ${container} ${object} | grep ETag | awk '{print $2}'`
    if [ "${ETag}" = "" ]; then
        >&2 echo "Unable to get ETag"
        exit 1
    fi

    md5=`md5sum ${object} | awk '{print $1}'`
    if [ "${md5}" = "" ]; then
        >&2 echo "Unable to get MD5"
        exit 2
    fi

    if [ "${md5}" != "${ETag}" ]; then
        >&2 echo "The local and remote copy of ${object} don't have the save checksum"
        exit 10
    fi

    exit 0

.. Links:

.. _`SURFsara helpdesk`: https://www.surf.nl/en/about-surf/contact/helpdesk-surfsara-services/index.html

.. _`SURFsara application form`: https://e-infra.surfsara.nl/
