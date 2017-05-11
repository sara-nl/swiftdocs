.. _how-to-use-swift:

****************
How to use SWIFT
****************

In this page you will find documentation about the different SWIFT clients that are available.

.. contents:: 
    :depth: 10

=========================
Swift Command line client
=========================
There is a swift commandline client written in python. You may find more information about this at: https://www.swiftstack.com/docs/integration/python-swiftclient.html. This page will provide information on how to install the client and how to use it.

On this page there are some examples about how to use the :ref:`Python SWIFT client <python-swift-client>`.

====
Curl
====
Information about accessing SWIFT through the **curl** command is given on the :ref:`curl <curl>` page.

==========
S3 clients
==========
S3curl can be downloaded from https://github.com/rtdp/s3curl.

More information on S3 clients may be found at the :ref:`S3 <s3>` page.

=========
Cyberduck
=========
Information about accessing SWIFT through Cyberduck is provided on the :ref:`cyberduck <cyberduck>` page.

==============
Python Library
==============
The :ref:`python library <pythonlibrary>` page gives you information on the python-swiftclient library.

===
API
===
SWIFT offers a REST API. Information about this API and some examples are described at the :ref:`API <api>` page.

=========
Cloudfuse
=========
It is possible to mount SWIFT object storage as a file system. The :ref:`cloudfuse <cloudfuse>` page has more information.

=========
Duplicity
=========
Duplicity is a backup tool that amongst others supports cloud storage systems. More information about this can be found at the :ref:`duplicity <dupl>` page.

======
Rclone
======
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
Owncloud/Nextcloud
==================
It is possible to connect SWIFT to an Owncloud or Nextcloud sync-and-share service as external storage. How you can do this is described at the :ref:`Owncloud/Nextcloud <owncloudnextcloud>` page.
