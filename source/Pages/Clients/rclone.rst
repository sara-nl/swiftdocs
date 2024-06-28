.. _rclone:

******
Rclone
******

In this page you will find documentation about rclone. Rclone is a command line programme to manage files on cloud storages. It runs on various platforms like Windows, Linux and OSX. It features:

* MD5/SHA1 hashes checked at all times for file integrity
* Timestamps preserved on files
* Partial syncs supported on a whole file basis
* Copy mode to just copy new/changed files
* Sync (one way) mode to make a directory identical
* Check mode to check for file hash equality
* Can sync to and from network, eg two different cloud accounts
* Optional encryption (Crypt)
* Optional FUSE mount (rclone mount)
* Optional GUI

Information on how to install rclone and other things may be found at: https://rclone.org. Rclone is available for various platforms like deb- or rpm-based linux distro's and Windows. More swift related information is available at: https://rclone.org/swift.

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
Configuration
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

Users using keystone coupled with their SURF Central User Administration (CUA) account should provide the value **CuaUsers** for *domain* and *tenant_domain*. Users having a local keystone account can leave the **default** values.

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
     region = NL
     endpoint = https://proxy.swift.surfsara.nl
     location_constraint = NL
     acl = private
     server_side_encryption =
     storage_class =

By default this file resides in: **.config/rclone/rclone.conf**. 

If you want to put the **rclone.conf** file in a non-standard place, then that is possible too, but then you need to run your rclone commands in the following manner:

.. code-block:: console

    rclone --config /path/to/rclone.conf <command> .......

Another possibility is is setting an environment variable like:

.. code-block:: console

   export RCLONE_CONFIG=/path/to/rclone.conf

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

    rclone mount --daemon swift:[container] /path/to/local/mount

You can unmount this file system by:

.. code-block:: console

     fusermount -u /path/to/local/mount

====================================
Use rclone as GUI for object storage
====================================

Rclone can also provide you with a GUI for object storage. This GUI can be 
started from the commandline. It will startup a web server on your computer 
to which you can connect using a browser. Then you have to connect to: 
**http://127.0.0.1:5572**

Since it starts up a web server 
you can protect this server by a username and password that you select yourself.
Below you can see the command to startup the web server with a user name and 
password.

.. code-block:: console

    rclone rcd --rc-web-gui --rc-user <user name> --rc-pass <password>

If you do not want to set a username and password for your then you can startup
the web server by the following command:

.. code-block:: console

    rclone rcd --rc-web-gui --rc-no-auth
