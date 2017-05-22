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


OS X
----

If you use Apple OS X, you may run into "System Integrity Protection" making installation hard. The easiest way, is to install the swift client into your home dir with ``--user`` and if needed ``--ignore-installed``, and make sure python uses that instead of the system version.

First, install your personal version of setuptools:

.. code-block:: console

    pip install --ignore-installed --user setuptools

Add these lines to your .profile:

.. code-block:: console

    export PATH=~/Library/Python/2.7/bin:$PATH
    export MANPATH=~/Library/Python/2.7/share/man:$MANPATH

Then create a file ~/Library/Python/2.7/lib/python/site-packages/fix_mac_path.pth with this line:

.. code-block:: console

    import sys; std_paths=[p for p in sys.path if p.startswith('/System/') and not '/Extras/' in p]; sys.path=[p for p in sys.path if not p.startswith('/System/')]+std_paths

Then install the swift client:

.. code-block:: console

    pip install --user python-swiftclient

If you want to change your password, install also the openstack client

.. code-block:: console

    pip install --user --ignore-installed python-openstackclient

For more info, check the excellent answer by Matthias Fripp on https://apple.stackexchange.com/questions/209572/how-to-use-pip-after-the-os-x-el-capitan-upgrade.

Examples
--------

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


===============================
Owncloud and Nextcloud coupling
===============================
It is possible to connect SWIFT to an Owncloud or Nextcloud sync-and-share service as external storage. How you can do this is described at the :ref:`owncloud <owncloud>` page.
