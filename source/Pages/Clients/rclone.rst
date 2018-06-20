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
* `Sync <https://rclone.org/commands/rclone_sync/>`_ (one way) mode to make a directory identical
* `Check <https://rclone.org/commands/rclone_check/>`_ mode to check for file hash equality
* Can sync to and from network, eg two different cloud accounts
* Optional encryption ( `Crypt <https://rclone.org/crypt/>`_ )
* Optional FUSE mount ( `rclone mount <https://rclone.org/commands/rclone_mount/>`_ )

.. contents:: 
    :depth: 4

=============
Authorisation
=============

You can use both the SWIFT protocol as well as the S3 protocol to access the system. Rclone needs some variables set in order to work. You can set these in the **rclone.conf** file. When you use SWIFT the **rclone.conf** file can have the following contents:

.. code-block:: console

    [swift]
    type = swift
    user = <user name>
    key = <password>
    auth = https://proxy.swift.surfsara.nl:5000/v3
    domain = default
    tenant = <project name>
    tenant_domain = default
    region = RegionOne
    storage_url = <storage url>
    auth_version = 3

Users using keystone coupled with their SURFsara Central User Administration (CUA) account should provide the value **CuaUsers** for *domain* and *tenant_domain*. Users having a local keystone account can leave the **default** values.

Here **<storage url>** is the url of the storage system that can be found using the swift commandline client or a script that can be downloaded from :download:`get_token_and_storage_url.sh <../../Scripts/bash/get_token_and_storage_url.sh>`

This **rclone.conf** can be generated interactively by running the command:

.. code-block:: console

    rclone config

Using the S3 protocol the **rclone.conf** file looks like this:

.. code-block:: console

   [S3]
   type = s3
   env_auth = false
   access_key_id = <access key>
   secret_access_key = <secret key>
   region = other-v2-signature
   endpoint = https://proxy.swift.surfsara.nl
   location_constraint = NL
   acl = private
   server_side_encryption =
   storage_class =

By default this file resides in: **.config/rclone/rclone.conf**. 

If you want to put the **rclone.conf** file in a non-standard place, then that is possible too, but then you need to run your rclone commands in the following manner:

.. code-block:: console

    rclone --config /path/to/rclone.conf <command> .......

Make sure that this file is only readable by you.

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

==============================================
Use rclone to mount file systems in user space
==============================================

Using rclone to mount a file system in user space is done as follows:

.. code-block:: console

    rclone mount swift:[container] /path/to/local/mount

You can unmount this file system by:

.. code-block:: console

     fusermount -u /path/to/local/mount
