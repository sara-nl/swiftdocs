.. _goofys:

******
Goofys
******

In this page you will find documentation on how to mount SWIFT object storage as a normal file system through **goofys** in user space.

Using goofys a bucket can be mounted as a filesystem using the S3 protocol on linux systems.

.. contents:: 
    :depth: 4

============
Installation
============

Information on how to install goofys may be found at: https://github.com/kahing/goofys#installation.

============
Configuration
============

1. Create a file ~/.aws/credentials with the following content:

.. code-block:: console

    [default]
    aws_access_key_id = <access key>
    aws_secret_access_key = <secret keys>
    region = NL

Don't forget:

.. code-block:: console

    chmod 600 ~/.aws/credentials

========================
Mounting the file system
========================

.. code-block:: console

    goofys --endpoint https://proxy.swift.surfsara.nl <bucket> <mount point>

==========================
Unmounting the file system
==========================

Unmounting the file system is done by:

.. code-block:: console

    fusermount -u <mount point>

