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

===========================================
Upload/Download an object to/from container
===========================================

Uploading an object:

.. code-block:: console

    curl -i -T myobject -X PUT -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

Downloading an object:

.. code-block:: console

    curl -s -S -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject -O

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

Static Large Objects
--------------------

Suppose we have a 100MB file, called **file**,  that is uploaded in three chunks.
Create a container for the big file and a separate container for the segments:

.. code-block:: console

    curl -i -X PUT -H "x-auth-token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer
    curl -i -X PUT -H "x-auth-token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer_segments

Split the big file into 40MB chunks

.. code-block:: console

    split -b 40000 file

The file is now split up in three files called **xaa**, **xab**, **xac**. Upload the three chunks to the segments container:

.. code-block:: console

    -rw-r--r-- 1 ron ron 100000000 apr 24 18:21 file
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xaa
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xab
    -rw-r--r-- 1 ron ron  20000000 apr 24 18:39 xac

Upload the three segments to the segments container:

    curl -i -X PUT -H "x-auth-token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer_segments/xaa --data-binary @xaa
    curl -i -X PUT -H "x-auth-token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer_segments/xab --data-binary @xab
    curl -i -X PUT -H "x-auth-token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer_segments/xac --data-binary @xac

Compute the md5 checksum of the three chunks:

.. code-block:: console

    48e9a108a3ec623652e7988af2f88867  xaa
    48e9a108a3ec623652e7988af2f88867  xab
    10e4462c9d0b08e7f0b304c4fbfeafa3  xac

Create the manifest file:

.. code-block:: console

    MANIFEST="["

    for sp in /mybigfilescontainer_segments/xaa /mybigfilescontainer_segments/xab /mybigfilescontainer_segments/xac; do

        ETAG=$(curl -I -s -H "X-Auth-Token: ${OS_AUTH_TOKEN}" "${OS_STORAGE_URL}$sp" | perl -ane '/Etag:/ and print $F[1];');
        SIZE=$(curl -I -s -H "X-Auth-Token: ${OS_AUTH_TOKEN}" "${OS_STORAGE_URL}$sp" | perl -ane '/Content-Length:/ and print $F[1];');
        SEGMENT="{\"path\":\"$sp\",\"etag\":\"$ETAG\",\"size_bytes\":$SIZE}";
        [ "$MANIFEST" != "[" ] && MANIFEST="$MANIFEST,";   MANIFEST="$MANIFEST$SEGMENT";

    done
    
    MANIFEST="${MANIFEST}]"

This generates a manifest file like this:

.. code-block:: console

    [{"path":"/mybigfilescontainer_segments/xaa",
      "etag":"48e9a108a3ec623652e7988af2f88867",
      "size_bytes":40000000},
     {"path":"/mybigfilescontainer_segments/xab",
      "etag":"48e9a108a3ec623652e7988af2f88867",
      "size_bytes":40000000},
     {"path":"/mybigfilescontainer_segments/xac",
      "etag":"10e4462c9d0b08e7f0b304c4fbfeafa3",
      "size_bytes":20000000}]

Then upload the manifest file like this:

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer/file?multipart-manifest=put --data-binary "$MANIFEST"
    
==============
Copy an object
==============

.. code-block:: console

    curl -i -X COPY -H "X-Auth-Token: <token>" -H "Destination: anothercontainer/myobject" <storage url>/mycontainer/myobject

===============
Bulk operations
===============

You can upload a tarball which will be extracted by SWIFT.

.. image:: /Images/bulk_upload.png

It is possible to do a bulk deletion. First you create a text file with all the containers and objects to be deleted. After that everything goes as follows:

.. image:: /Images/bulk_deletion.png

=================
Object versioning
=================
TBD
