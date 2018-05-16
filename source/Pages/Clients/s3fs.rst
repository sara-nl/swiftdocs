.. _s3fs:

****
S3FS
****

In this page you will find documentation on how to mount SWIFT object storage as a normal file system through **s3fs** in user space. Using s3fs can be mounted as a filesystem using the S3 protocol on linux systems using fuse.
 
It features:

- large subset of POSIX including reading/writing files, directories, symlinks, mode, uid/gid, and extended attributes
- large files via multi-part upload
- renames via server-side copy
- optional server-side encryption
- data integrity via MD5 hashes
- in-memory metadata caching
- local disk data caching
- authenticate via v2 or v4 signatures

More information may be found at: https://github.com/s3fs-fuse/s3fs-fuse/wiki/Fuse-Over-Amazon

.. contents:: 
    :depth: 4

============
Installation
============

Documentation on how to install s3fs can be found at: https://github.com/s3fs-fuse/s3fs-fuse. 

============
Configuration
============

1. Create a file ${HOME}/.passwd-s3fs with the following content:

.. code-block:: console

    <access key>:<secret key>

Don't forget:

.. code-block:: console

    chmod 600 ${HOME}/.passwd-s3fs

========================
Mounting the file system
========================

1. This is done as follows:

.. code-block:: console

    s3fs <bucket> <mount point> -o url=https://proxy.swift.surfsara.nl -o use_path_request_style

==========================
Unmounting the file system
==========================

Unmounting the file system is done by:

.. code-block:: console

    fusermount -u <mount point>
