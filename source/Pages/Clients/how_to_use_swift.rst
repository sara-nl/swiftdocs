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

More detailed information on what is and is not supported may be found at: https://docs.openstack.org/swift/latest/s3_compat.html


.. contents:: 
    :depth: 10


==============
Authentication
==============
In order to use the SWIFT service you need a user name and a password. SWIFT supports so-called **v3** authentication. For v3 authentication, you have **projects**. Unless we agree upon something else, your project name is the same as your user name. In v3 authentication there are **domains** for both users and projects. If you have an account in SURFsara's Central User Administration (CUA) system, then both your **project domain** as your **user domain** is **CuaUsers**. When you only have a local account, then both domains are equal to **Default**. 

In order to be able to use the S3 protocol, you need to get to create so-called EC2 credentials, i.e. an access key and a secret key. How this works is described in :ref:`EC2 credentials for S3 <s3cred>`.


====================
Command line clients
====================

* Swift
   * :ref:`Python SWIFT client <python-swift-client>`.
   * :ref:`Curl <curl>`
   * :ref:`rclone <rclone>`

* S3
   * :ref:`S3cmd <s3cmd>`
   * AWS S3 client (:ref:`awscli <awscli>`)
   * :ref:`S5cmd <s5cmd>`, for parallel file transfers
   * :ref:`rclone <rclone>`


====
GUIs
====

* :ref:`Cyberduck <cyberduck>`

====================
Mounted file systems
====================

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


.. ===============================
   Owncloud and Nextcloud coupling
   ===============================

..   .. note:: **Note:** Since Nextcloud and Owncloud only support keystone V2 authentication, this will only work for users having a local keystone account.

..   It is possible to connect SWIFT to an Owncloud or Nextcloud sync-and-share service as external storage. How you can do this is described at the :ref:`owncloud <owncloud>` page.

..   It is also possible to connect Owncloud or Nextcloud using the S3 protocol. Here the restriction to only local users does not apply.
