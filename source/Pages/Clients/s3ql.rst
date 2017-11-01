.. _s3ql:

****
S3QL
****

In this page you will find documentation on how to mount SWIFT object storage as a normal file system through **s3ql** in user space.

S3QL has features like compression, encryption, data de-duplication, immutable trees and snapshotting which make it especially suitable for online backup and archival.

Using s3ql can be mounted as a filesystem using swift's own native protocol and S3 on linux systems.

.. note:: **Important:** Since s3ql only supports keystone V2 authentication, this will only work for users having a local keystone account when mounting using the swift protocol. Such a limitation does not exist using S3.

.. contents:: 
    :depth: 4

============
Installation
============

Documentation on how to install s3ql can be found at: https://bitbucket.org/nikratio/s3ql/wiki/Home. On linux, your distro often has the s3ql package in their repos, see: https://bitbucket.org/nikratio/s3ql/wiki/Installation. There is also a user guide: http://www.rath.org/s3ql-docs/index.html.

============
Configuration
============

1. Create a file ${HOME}/.s3ql/authinfo2 with the following content:

For swift:

.. code-block:: console

    [swift]
    backend-login: <project name>:<user name>
    backend-password: <password>
    storage-url: swiftks://proxy.swift.surfsara.nl:5000/RegionOne:<container name>

For S3:

.. code-block:: console

    [s3]
    backend-login: <access key>
    backend-password: <secret keys>
    storage-url: s3c://proxy.swift.surfsara.nl:443/<bucket>
    fs-passphrase: <password>

The **fs-passphrase** is the password used to encrypt the randomly generated master key. This makes sure that s3ql encrypts data before it uploads the data to SWIFT.

Don't forget:

.. code-block:: console

    chmod 600 ${HOME}/.s3ql/authinfo2

========================
Mounting the file system
========================

1. Create a directory that is to be mounted

.. code-block:: console

    mkdir /path/to/mount

2. Mount the SWIFT object storage

For SWIFT:

.. code-block:: console

    mount.s3ql swiftks://proxy.swift.surfsara.nl:5000/RegionOne:<container name> /path/to/mount

For S3:

.. code-block:: console

    moun.s3ql s3c://proxy.swift.surfsara.nl:443/<bucket> /path/to/mount

==========================
Unmounting the file system
==========================

Unmounting thee file system is done by:

.. code-block:: console

    umount.s3ql /path/to/mount
