.. _how-to-use-swift:

.. image:: /Images/objectstore3.png
           :width: 300px
           :align: right

****************
How to use SWIFT
****************

In this page you will find documentation about the different SWIFT clients that are available. SWIFT can be addressed with its own native protocol and with the S3 protocol. With respect to S3 the following is supported:


- Support AWS Signature Version 2, 4 (Version 4 is ready for only keystone)
- Support Services APIs (GET)
- Support Bucket APIs (GET/PUT/DELETE/HEAD)
- Support Object APIs (GET/PUT/DELETE/HEAD)
- Support Multipart Upload (required SLO middleware support)
- Support S3 ACL (under development)


.. contents:: 
    :depth: 10


==============
Authentication
==============
In order to use the SWIFT service you need a user name and a password. But that is not the only thing that you need. SWIFT supports two versions of authentication, **v2** and **v3**. For v2 authentication you need a so-called **tenant**. Unless we agree on something else with you, your tenant is the same as your user name. For v3 authentication, we do not have tenants but **projects**. They are the same. So, again, unless we agree upon something else, your project name is the same as your user name. In addition to v2 authentication, in v3 authentication we also have **domains** for both users and projects. If you have an account in SURFsara's Central User Administration (CUA) system, then both your **project domain** as your **user domain** is **CuaUsers**. When you only have a local account, then both domains are equal to **Default**. In order to be able to use the S3 protocol, you need to get to create so-called EC2 credentials, i.e. an access key and a secret key. How this works is described in :ref:`EC2 credentials for S3 <s3cred>`.

====================
Command line clients
====================

Swift command line client
------------------------

On this page there is info on how to install and use the :ref:`Python SWIFT client <python-swift-client>`.

S3 command line client s3cmd
---------------------------

Information on s3cmd may be found at the :ref:`S3cmd <s3cmd>` page.

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

It is also possible to connect Owncloud or Nextcloud using the S3 protocol. Here the restriction to only local users does not apply.

========================
Serving Static Web Pages
========================

SWIFT offers the possibility to serve data in containers as a static web site. The :ref:`staticweb <staticweb>` page has more.
