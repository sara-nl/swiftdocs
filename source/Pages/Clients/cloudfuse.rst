.. _cloudfuse:

*********
Cloudfuse
*********

In this page you will find documentation on how to mount SWIFT object storage as a normal file system through **cloudfuse**.

.. contents:: 
    :depth: 4

============
Installation
============

Documentation on how to install cloudfuse can be found at: https://www.cloudvps.com/customer-service/knowledge-base/cloudfuse-mount-your-object-store-in-linux for CentOS/Redhat based distro's or for both Redhat-type and Debian-type distro's have a look at: https://knowledgelayer.softlayer.com/learning/how-mount-object-storage. 

============
Configuration
============

1. Create a file ${HOME}/.cloudfuse with the following content:

.. code-block:: console

    username=<user name>
    tenant=<project name>
    password=<password>
    authurl=https://proxy.swift.surfsara.nl/auth/v2.0
    verify_ssl=True

Don't forget:

.. code-block:: console

    chmod 600 ${HOME}/.cloudfuse

2. Create a directory that is to be mounted

.. code-block:: console

    mkdir /path/to/mount

3. Mount the SWIFT object storage

.. code-block:: console

    cloudfuse -o auto_unmount /path/to/mount
