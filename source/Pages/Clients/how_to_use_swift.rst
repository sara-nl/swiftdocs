.. _how-to-use-swift:

****************
How to use SWIFT
****************

In this page you will find documentation about the different SWIFT clients that are available.

.. contents:: 
    :depth: 10

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

S3 clients
----------

Curl
----

Information about accessing SWIFT through the **curl** command is given on the :ref:`curl pages <curl>`.

Libraries
---------

API
---

SWIFT offers a REST API. Information about this API and some examples are described at the :ref:`API page <api>`.

Duplicity
---------

Duplicity is a backup tool that amongst others supports cloud storage systems. More information about this can be found at the :ref:`duplicity page <dupl>`.

Rclone
------

Rclone is the rsync for cloud storage. Here is more information on how to use rclone on the :ref:`rclone page <rclone>`.

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
