.. _how-to-use-swift:

****************
How to use SWIFT
****************

In this page you will find documentation about the different SWIFT clients that are available.

.. contents:: 
    :depth: 4

=======
Clients
=======

Swift Command line client
-------------------------
There is a swift commandline client written in python. You may find more information about this at: https://www.swiftstack.com/docs/integration/python-swiftclient.html. This page will provide information on how to install the client and how to use it.
If you want to know more about all options of the *swift* command. Just type in the command

.. code-block:: console

	swift help

Here are some examples about how to use the :ref:`Python SWIFT client <python-swift-client>`.

Curl
----

API
---

S3 clients
----------

Duplicity
---------

Duplicity is a backup tool that amongst others supports cloud storage systems. More information about this can be found at the :ref:`duplicity <duplicity>`_ documentation.

Rclone
------

Rclone is the rsync for cloud storage. Here is more information on how to use :ref:`rclone <rclone>`.

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


Owncloud/Nextcloud
------------------
