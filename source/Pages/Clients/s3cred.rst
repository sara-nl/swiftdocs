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

.. code-block:: console

    # openstack ec2 credentials create
    +------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
    | Field      | Value                                                                                                                                               |
    +------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
    | access     | 9c7ea003adef4431adef6772ff4385de                                                                                                                    |
    | links      | {u'self': u'https://proxy.swift.surfsara.nl:35357/v3/users/bd47bc49ea29344889234ffefa818e8576/credentials/OS-EC2/9c7ea003adef4431adef6772ff4385de'} |
    | project_id | 05b2aaf3746adfe932726d88649d95fe                                                                                                                    |
    | secret     | e330ef98dddf45885efb89a3aaf3c091                                                                                                                    |
    | trust_id   | None                                                                                                                                                |
    | user_id    | bd47bc49ea29344889234ffefa818e8576                                                                                                                  |
    +------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Here **access** is your access key and **secret** is your secret key.

=================
Listing your keys
=================

To list all you EC2 keys you can type the follwoing command:

.. code-block:: console

    # openstack ec2 credentials list
    +----------------------------------+----------------------------------+----------------------------------+------------------------------------+
    | Access                           | Secret                           | Project ID                       | User ID                            |
    +----------------------------------+----------------------------------+----------------------------------+------------------------------------+
    | 9c7ea003adef4431adef6772ff4385de | e330ef98dddf45885efb89a3aaf3c091 | 05b2aaf3746adfe932726d88649d95fe | bd47bc49ea29344889234ffefa818e8576 |
    +----------------------------------+----------------------------------+----------------------------------+------------------------------------+

It is perfectly OK to have more than one key pair.

=======================================
Show information about tou your keypair
=======================================

To show you the information about a key pair you can do the following:

.. code-block:: console

    openstack ec2 credentials show <access key>

So, for example:

.. code-block:: console

    # openstack ec2 credentials show 9c7ea003adef4431adef6772ff4385de
    +------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
    | Field      | Value                                                                                                                                               |
    +------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
    | access     | 9c7ea003adef4431adef6772ff4385de                                                                                                                    |
    | links      | {u'self': u'https://proxy.swift.surfsara.nl:35357/v3/users/bd47bc49ea29344889234ffefa818e8576/credentials/OS-EC2/9c7ea003adef4431adef6772ff4385de'} |
    | project_id | 05b2aaf3746adfe932726d88649d95fe                                                                                                                    |
    | secret     | e330ef98dddf45885efb89a3aaf3c091                                                                                                                    |
    | trust_id   | None                                                                                                                                                |
    | user_id    | bd47bc49ea29344889234ffefa818e8576                                                                                                                  |
    +------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

========================
Delete an EC2 credential
========================

You can delete an EC2 credential in the following way:

.. code-block:: console

    openstack ec2 credentials delete <access key>

So you have, for example:

.. code-block:: console

    # openstack ec2 credentials delete 9c7ea003adef4431adef6772ff4385de
    # openstack ec2 credentials show 9c7ea003adef4431adef6772ff4385de
    Could not find credential: 8983bd0b0164522463820384625c16e78f3d29c2546392dde4535d0e49066b9d. (HTTP 404) (Request-ID: req-786378da-027d-4ff2-ac2e-25c36a9cf5a5)
