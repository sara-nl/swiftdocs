.. _python-swift-client:

*******************
Python SWIFT client
*******************

In this page you will find documentation about the Python SWIFT client that are available.

.. contents:: 
    :depth: 4

=====
Usage
=====

Now the usage of the **swift** commandline tools is like:

.. code-block:: console

         swift [options] <command> [--help] [<command options>]

More details and examples are provided below.

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

Apart from using your user name and password, it is also possible to generate a token that is valid for 24 hours. This may be handy if you running the script elsewhere on a batch system and you don't want to send you username and password with your batch job. You can use this token to access your data in SWIFT.

You can get a token in the following way:

.. image:: /Images/token.png

What you need is the **StorageURL** and the **Auth Token**. You can use these two to run the swift commands for the next 24 hours without supplying your user name and password.

.. code-block:: console

         swift --os-auth-token <TOKEN> --os-storage-url <STORAGE URL> [options] <command> [--help] [<command options>]

For example:
        
.. image:: /Images/list_token.png

What you can do is for example:

.. image:: /Images/auth.png

and do the exports and run:

.. code-block:: console

         swift --os-auth-token ${OS_AUTH_TOKEN} --os-storage-url ${OS_STORAGE_URL} [options] <command> [--help] [<command options>]

==================
Create a container
==================

.. image:: /Images/make_container.png
           :width: 600px


A container can be created by the following command:

.. code-block:: console

         swift post mycontainer

=============================================
Upload/Download an object to/from a container
=============================================

.. image:: /Images/upload.jpg
           :width: 600px


.. code-block:: console

         swift upload mycontainer myobject

If the container **mycontainer** does not exist yet, then it will be created. Downloading an object from a container goes as follows:

.. code-block:: console

         swift download mycontainer myobject

Downloading the whole content of a container is done by:

.. code-block:: console

         swift download mycontainer


=================
Getting metadata
=================

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

=================================
List the containers in an account
=================================

The containers in an account can be listed like:

.. code-block:: console

         swift list

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

========================================================
Set and get your own metadata for containers and objects
========================================================

To set and get metadata for an container goes in the following manner:

.. image:: /Images/metadata_container.png

Setting and getting metadata for an object works in an identical fashion.

============================
Uploading large files (>5GB)
============================

It is only possible to upload objects with the size of at most 5GB in one go to SWIFT. It is possible to up and download larger objects when the large object is uploaded in chunks. For the python SWIFT client you can upload an object larger than 5GB in the following way:

.. image:: /Images/bigfiles.png

For downloading you can just proceed as usual. For more information on this we refer to the documentation on large objects at: https://docs.openstack.org/developer/swift/overview_large_objects.html

=================
Object versioning
=================
TBD

=======================================================
Script to verify MD5 checksums of local and remote copy
=======================================================

.. code-block:: bash

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
        >&2 echo "The local and remote copy of ${object} don't have the same checksum"
        exit 10
    fi

    exit 0
