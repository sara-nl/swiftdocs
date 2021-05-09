.. _awscli:

******
awscli
******

In this page you will find documentation about the AWS commandline client.

.. contents:: 
    :depth: 4

============
Installation
============

The AWS commandline client can be installed in the following way:

.. code-block:: console

       pip install awscli-plugin-endpoint
       pip install awscli

=============
Configuration
=============

First you need to create a file ~/.aws/config with the following content:

.. code-block:: console

       [plugins]
       endpoint = awscli_plugin_endpoint

       [profile default]
       aws_access_key_id = <access key>
       aws_secret_access_key = <secret key>
       region = NL
       s3 = 
            endpoint_url = https://proxy.swift.surfsara.nl
            addressing_style = path
            signature_version = s3v4
            payload_signing_enabled = true
       s3api = 
            endpoint_url = https://proxy.swift.surfsara.nl
            addressing_style = path
            signature_version = s3v4
            payload_signing_enabled = true

Don't forget to:

.. code-block:: console

    chmod 600 ~/.aws/config

=====
Usage
=====

Information on how to use the **aswcli** may be found at: `s3`_ and `s3api`_.

====================
S3 Bucket versioning
====================

It is possible to enable S3 bucket versioning. This can be enabled per bucket. 
If you do this then when you overwrite an existing object, then you can still retrieve the previously overwritten version. 
In addition, when you accidentally delete an object, then you can still restore the deleted object when you have bucket versioning enabled.

.. note:: **Note:** No object will ever be thrown away. This means that you may end up with a lot of data in buckets where there is a lot of overwriting and deleting going on. So a manual cleanup may be necessary. Unfortunately, at the time of writing it is not possible to impose a life cycle policy so that versions are automatically cleaned up.

More detailed information on this may be found at: `s3versioning`_. Below we 
will provide an example on how to do this with the AWS commandline client.

Enabling and suspending bucket versioning
-----------------------------------------

You can enable versioning on the bucket in the following way:

.. image:: /Images/enabling_bucket_versioning.png

It is not possible to turn off bucket versioning completely. However, it is possible to suspend it. This can be done by:

.. code-block:: console

    aws s3api put-bucket-versioning --bucket <bucket name> --versioning-configuration Status=Suspended

Restoring a deleted object
--------------------------

Now if you, by accident, delete an object, then you can still retrieve it. Suppose we do the following:

.. image:: /Images/accidental_file_deletion.png

What you can do next is list the versions of the object that are available:

.. image:: /Images/list_versions.png

Here you see a so-called "Delete Marker" indicating that the object has been deleted. In order to restore the deleted object you simply have to delete this Delete Marker and you will have your object back. This is done in the following way:

.. image:: /Images/retrieve_lost_file.png

Working with multiple versions
------------------------------
Suppose we are uploading different versions of a file with the same name as shown below

.. image:: /Images/multipleversions.png

After that we can list these versions by:

.. image:: /Images/listing_versions2.png

Then we can get the most current version by:

.. image:: /Images/get_current_version.png

You can retrieve an earlier version by:

.. image:: /Images/get_other_version.png

Listing version information
---------------------------
You can list all available versions of a particular file including the version id, modification time and if it is the most current version or not in the following way

.. image:: /Images/listing_versions3.png

A maximum of 1000 objects are returned at one time. If you have more than 1000 objects in a bucket you may want to use a script like the one that is provided at: :download:`versions_listing.sh <../../Scripts/bash/versions_listing.sh>`
This script displays the object, version id, last modification time stamp, if it is the current version and if it is a delete marker.

Cleaning up a versioned bucket
------------------------------
If you want to completely remove a bucket with versioning enabled, then you need to cleanup all versions of the objects and delete markers first. After that you can remove the bucket using:

.. code-block:: console

    aws s3 rb s3://<bucket name>

A script that can be used to delete all object, versions of objects and delete markers is provided at: `delete_all_versions.py <../../Scripts/bash/delete_all_versions.py>`. Please use at your own risk.


.. Links:

.. _`s3`: https://docs.aws.amazon.com/cli/latest/reference/s3/index.html
.. _`s3api`: https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html
.. _`s3versioning`: https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html
