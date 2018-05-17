.. _how-to-use-swift:

.. image:: /Images/objectstore3.png
           :width: 300px
           :align: right

****************
How to use SWIFT
****************

In this page you will find documentation about the different SWIFT clients that are available.

.. contents:: 
    :depth: 10

====================
Command line clients
====================

Swift command line client
------------------------

There is a swift command line client written in python. You may find more information about this at: https://www.swiftstack.com/docs/integration/python-swiftclient.html. This page will provide information on how to install the client and how to use it. This page tells you how to install the client on various flavours of Linux. For windows it is rather similar. You need to install python2.7 on windows, see: https://www.howtogeek.com/197947/how-to-install-python-on-windows/. Do not forget to include python in your PATH. The modern versions of Python2.7 are shipped with pip, so for the rest the linux documentation can be followed.

For extra information on how to install de swift command line client on Mac OSX, please, have a look at: :ref:`Installation Instructions of the Python SWIFT Client on OSX <python-swift-client-osx>`.

On this page there is info on how to use the :ref:`Python SWIFT client <python-swift-client>`.

S3 command line client s3cmd
---------------------------

Information on s3cmd may be found at the :ref:`S3 <s3>` page.

Curl
----

Information about accessing SWIFT through the **curl** command is given on the :ref:`curl <curl>` page.

====
GUIs
====

Cyberduck
---------

Information about accessing SWIFT through Cyberduck is provided on the :ref:`cyberduck <cyberduck>` page.

====================
Mounted file systems
====================

Cloudfuse
---------

.. note:: **Important:** Since Cloudfuse only supports keystone V2 authentication, this will only work for users having a local keystone account.

It is possible to mount SWIFT object storage as a file system with cloudfuse. The :ref:`cloudfuse <cloudfuse>` page has more information.

S3QL
----

It is possible to mount SWIFT object storage as a file system with s3ql both using swift's native protocol and S3. 

S3QL has features like compression, encryption, data de-duplication, immutable trees and snapshotting which make it especially suitable for online backup and archival.

The :ref:`s3ql <s3ql>` page has more information.

S3FS
----

It is possible to mount SWIFT object storage as a file system with s3fs using the S3 protocol. 

The :ref:`s3fs <s3fs>` page has more information.

=======
Backups
=======

Duplicity
---------

Duplicity is a backup tool that amongst others supports cloud storage systems. More information about this can be found at the :ref:`duplicity <dupl>` page.

===============
Synchronisation
===============

Rclone
------

Rclone is the rsync for cloud storage. Here is more information on how to use rclone on the :ref:`rclone <rclone>` page.

It features:

* MD5/SHA1 hashes checked at all times for file integrity
* Timestamps preserved on files
* Partial syncs supported on a whole file basis
* Copy mode to just copy new/changed files
* Sync (one way) mode to make a directory identical
* Check mode to check for file hash equality
* Can sync to and from network, eg two different cloud accounts
* Optional encryption (Crypt)
* Optional FUSE mount (rclone mount)

==================
Libraries and APIs
==================

Python Library
--------------

The :ref:`python library <pythonlibrary>` page gives you information on the python-swiftclient library.


REST API
--------

SWIFT offers a REST API. Information about this API and some examples are described at the :ref:`API <api>` page.

Boto3
-----

Boto3 is the AWS SDK for python developed by Amazon. It contains of course an S3 part to access object stores. At :ref:`boto3 <boto3>` has information on how to use it.


===============================
Owncloud and Nextcloud coupling
===============================

.. note:: **Note:** Since Nextcloud and Owncloud only support keystone V2 authentication, this will only work for users having a local keystone account.

It is possible to connect SWIFT to an Owncloud or Nextcloud sync-and-share service as external storage. How you can do this is described at the :ref:`owncloud <owncloud>` page.

