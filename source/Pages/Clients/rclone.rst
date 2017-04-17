.. _rclone:

******
rclone
******

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
* Optional FUSE mount ( `rclone mount <https://rclone.org/commands/rclone_mount/>`_ )

.. contents:: 
    :depth: 4

=============
Authorisation
=============

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
    storage_url = <storage url>
    auth_version =

Here **<storage url>** is the url of the storage system that can be found using the command:

.. code-block:: console

    curl -i -s -H "X-Auth-User: <user name>" -H "X-Auth-Key: <password>" https://proxy.swift.surfsara.nl/auth/v1.0  | grep X-Storage-Url

Don't for get to:

.. code-block:: console

    chmod 600 ${HOME}/.rclone.conf

==============================================
Copy source directory to destination container
==============================================

.. code-block:: console

    rclone copy /my/folder swift:mycontainer

Copy the source to the destination. Doesn’t transfer unchanged files, testing by size and modification time or MD5SUM. Doesn’t delete files from the destination.

If **mycontainer** doesn’t exist, it is created and the contents of **/my/folder** go there.

================================================
Sync source directory with destination container
================================================

.. code-block:: console

    rclone sync /my/folder swift:mycontainer

Sync the source to the destination, changing the destination only. Doesn’t transfer unchanged files, testing by size and modification time or MD5SUM. Destination is updated to match source, including deleting files if necessary.


.. note:: **Important:** Since this can cause data loss, test first with the --dry-run flag to see exactly what would be copied and deleted.

Note that files in the destination won’t be deleted if there were any errors at any point.

If **mycontainer** doesn’t exist, it is created and the contents of **/my/folder** go there.

==================================================
Check if files in the source and destination match
==================================================

.. code-block:: console

    rclone check /my/folder swift:mycontainer

Checks the files in the source and destination match. It compares sizes and hashes (MD5 or SHA1) and logs a report of files which don’t match. It doesn’t alter the source or destination.
