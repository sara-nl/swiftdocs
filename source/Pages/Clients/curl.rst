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

It is only possible to upload objects with the size of at most 5GB in one go to SWIFT. It is possible to up and download larger objects. For this we refer to the documentation on large objects at: https://docs.openstack.org/developer/swift/overview_large_objects.html. 

There are dynamic large objects and static large objects. 
- **Static Large Object** - Relies on a user provided manifest file. Advantageous for use cases when the developer wants to “mashup” objects from multiple containers and reference them in a self-generated manifest file. This gives you immediate access to the concatenated object after the manifest is accepted. Uploading segments into separate containers provides the opportunity for improved concurrent upload speeds. On the downside, the concatenated object’s definition is frozen until the manifest is replaced.
- **Dynamic Large Object** - Relies on a container-listing zero-byte manifest file. Advantageous for use cases when the developer might add/remove segments from the manifest (e.g. objects from the container) at any time. A few disadvantages include reliance on eventual consistent container listings which means there may be some delay before access to the full concatenated object is available. There is also a requirement for all segments to be in a single container, which can limit concurrent upload speeds.

This page: https://docs.openstack.org/developer/swift/api/large_objects.html#comparison-of-static-and-dynamic-large-objects gives an overview of the difference between dynamic large objects and static large objects.

Dynamic Large Objects
---------------------

Suppose we have a 100MB file, called **file**,  that is uploaded in three chunks or segments.
Create a container for the big file:

.. code-block:: console

    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer

Split the big file into 40MB chunks

.. code-block:: console

    split -b 40000 file

The file is now split up in three files called **xaa**, **xab**, **xac**. Upload the three chunks to the segments container:

.. code-block:: console

    -rw-r--r-- 1 ron ron 100000000 apr 24 18:21 file
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xaa
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xab
    -rw-r--r-- 1 ron ron  20000000 apr 24 18:39 xac

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer/file/001 --data-binary @xaa
    curl -i -X PUT -H "X-Auth-Token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer/file/002 --data-binary @xab
    curl -i -X PUT -H "X-Auth-Token: ${OS_AUTH_TOKEN}" ${OS_STORAGE_URL}/mybigfilescontainer/file/003 --data-binary @xac

Upload the manifest file:

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: ${OS_AUTH_TOKEN}" -H 'X-Object-Manifest: mybigfilescontainer/file/' ${OS_STORAGE_URL}/mybigfilescontainer/file --data-binary ''

Now you can download the file normally.

Static Large Objects
--------------------

Suppose we have a 100MB file, called **file**,  that is uploaded in three chunks.
Create a container for the big file and a separate container for the segments:

.. code-block:: console

    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer
    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments

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

.. code-block:: console

    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments/xaa --data-binary @xaa
    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments/xab --data-binary @xab
    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments/xac --data-binary @xac

Create the manifest file:

.. code-block:: bash

    MANIFEST="["

    for sp in /mybigfilescontainer_segments/xaa /mybigfilescontainer_segments/xab /mybigfilescontainer_segments/xac; do

        ETAG=$(curl -I -s -H "X-Auth-Token: ${<token>}" "${<storage url>}$sp" | perl -ane '/Etag:/ and print $F[1];');
        SIZE=$(curl -I -s -H "X-Auth-Token: ${<token>}" "${<storage url>}$sp" | perl -ane '/Content-Length:/ and print $F[1];');
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

    curl -i -X PUT -H "X-Auth-Token: ${<token>}" ${<storage url>}/mybigfilescontainer/file?multipart-manifest=put --data-binary "$MANIFEST"

After this you can download the file as normal.

The **ETag** of the whole file can be computed as:

.. code-block:: console

    echo -n 'etagoffirstsegmentetagofsecondsegmentetagofthirdsegment...' | md5sum

So in this case this would be:

.. image:: /Images/bigfilesmd5sum.png

Run the following command to throw away the file, the segments and the manifest file:
    
.. code-block:: console

    curl -i -X DELETE -H "X-Auth-Token: ${<token>}" ${<storage url>}/mybigfilescontainer/file?multipart-manifest=delete

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
