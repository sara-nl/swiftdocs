.. _s3cred:

**********************
EC2 credentials for S3
**********************

=============
Prerequisites
=============

On this page we will show you how to obtain and manage so-called EC2 credentials that you need to access SWIFT using the S3 protocol.

You need to make sure that you have the **python-openstackclient** installed. More information for the various platforms can be found at the following pages:

* :ref:`Installation Instructions of the Python SWIFT Client on Windows <python-swift-client-windows>`
* :ref:`Installation Instructions of the Python SWIFT Client on Linux <python-swift-client-linux>`
* :ref:`Installation Instructions of the Python SWIFT Client on OSX <python-swift-client-osx>`

==============
Authentication
==============

The following environment variables are useful to set if you don't want them to provide them all the time on the command line.

.. code-block:: console

    export OS_PROJECT_DOMAIN_NAME=Default
    export OS_USER_DOMAIN_NAME=Default
    export OS_PROJECT_NAME=<my project>
    export OS_USERNAME=<user name>
    export OS_PASSWORD=<password>
    export OS_AUTH_URL=https://proxy.swift.surfsara.nl:5000/v3
    export OS_IDENTITY_API_VERSION=3

This holds for local keystone users. Users using their account in the SURFsara Central User Administration (CUA) through keystone need the specify the following:

.. code-block:: console

    export OS_PROJECT_DOMAIN_NAME=CuaUsers
    export OS_USER_DOMAIN_NAME=CuaUsers

for the **OS_PROJECT_DOMAIN_NAME** and **OS_USER_DOMAIN_NAME** environment variables. Apart from using your user name and password, it is also possible to generate a token that is valid for 24 hours. This may be handy if you are running the script elsewhere on a batch system and you don't want to send you username and password with your batch job. You can use this token to access your data in SWIFT.

========================
Create an EC2 credential
========================

Now you can create a credential in the following way:

.. code-block:: console

    openstack ec2 credentials create

This should give you output like this:

.. image:: /Images/ec2_create_credentials.png

Here **access** is your access key and **secret** is your secret key.

=================
Listing your keys
=================

To list all you EC2 keys you can type the following command:

.. image:: /Images/ec2_list_credentials.png

It is perfectly OK to have more than one key pair.

===================================
Show information about your keypair
===================================

To show you the information about a key pair you can do the following:

.. code-block:: console

    openstack ec2 credentials show <access key>

So, for example:

.. image:: /Images/ec2_show_credentials.png

========================
Delete an EC2 credential
========================

You can delete an EC2 credential in the following way:

.. code-block:: console

    openstack ec2 credentials delete <access key>

So you have, for example:

.. image:: /Images/ec2_delete_credentials.png
