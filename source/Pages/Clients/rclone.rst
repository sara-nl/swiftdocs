.. _rclone:

*******************
rclone
*******************

In this page you will find documentation about rclone. Rclone is the rsync for cloud storage. Information on how to install rclone and other things may be found at: https://rclone.org. More swift related information is available at: https://rclone.org/swift.

Apart from being an rsync-type tool for cloud storage, it has the following features:

* MD5/SHA1 hashes checked at all times for file integrity
* Timestamps preserved on files
* Partial syncs supported on a whole file basis
* `Copy <https://rclone.org/commands/rclone_copy/>`_ mode to just copy new/changed files
* `Sync <https://rclone.org/commands/rclone_copy/>`_ (one way) mode to make a directory identical
* `Check <https://rclone.org/commands/rclone_check/>`_ mode to check for file hash equality
* Can sync to and from network, eg two different cloud accounts
* Optional encryption ( `Crypt <https://rclone.org/crypt/>`_ )
* Optional FUSE mount ( `rclone mount` <https://rclone.org/commands/rclone_mount/>`_ )

.. contents:: 
    :depth: 4

=============
Authorisation
=============

Rclone needs some variables set in order to work. You can set these in a **.rclone.conf** file in your home directory
Rclone needs some variables set in order to work. You can set these in a **.rclone.conf** file in your home directory. This file can have the following contents:

.. code-block:: console

    [swift]
    type = swift
    user = <user name>
    key = <password>
    auth = https://proxy.swift.surfsara.nl/auth/v1.0
    domain = default
    tenant = 
    tenant_domain = 
    region = 
    storage_url = https://proxy.swift.surfsara.nl/v1/<account>
    auth_version =

The name of your account can be found using the command:

.. code-block:: console

    curl -i -s -H "X-Auth-User: <user name>" -H "X-Auth-Key: <password>" https://proxy.swift.surfsara.nl/auth/v1.0  | grep X-Storage-Url | sed -e 's/.*\/AUTH/AUTH/'

