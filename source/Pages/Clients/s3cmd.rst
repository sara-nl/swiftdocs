.. _s3cmd:

***************************
S3 commandline client s3cmd
***************************

In this page you will find documentation about the S3 clients. Here we refer to **buckets**, this is the S3 term for **containers**. They are identical.

.. contents:: 
    :depth: 4

=====
s3cmd
=====

Information of **s3cmd** may be found at http://s3tools.org/s3cmd and https://github.com/s3tools/s3cmd/blob/master/README.md. 

Authentication
--------------
In your home directory you need to create a file called **.s3cfg** with a contents like:

.. code-block:: console

    [default]

    access_key = <access key>
    secret_key = <secret key>
    host_base = proxy.swift.surfsara.nl
    host_bucket = proxy.swift.surfsara.nl
    signature_v2 = True
    check_ssl_certificate = True
    check_ssl_hostname = True


Don't forget to:

.. code-block:: console

    chmod 600 ~/.s3cfg


Create a bucket
---------------

.. code-block:: console

    s3cmd mb s3://mybucket

Upload/Download an object to/from a bucket
------------------------------------------

An object can be uploaded to a bucket by the following command:

.. code-block:: console

    s3cmd put <file name> s3://mybucket/myobject

It can be downloaded by:

.. code-block:: console

    s3cmd get s3://mybucket/myobject

Getting metadata
----------------

The metadata of an object can be retrieved by:

.. image:: /Images/s3cmdinfo.png

Setting metadata
----------------

S3cmd can be used to set custom metadata during the upload of a file. This is shown below.

.. image:: /Images/s3cmdaddheader.png

Adding and modifying metadata
-----------------------------

Metadata can be added and modyfied in the following manner:

.. image:: /Images/s3cmdchangemetadata.png

Deleting metadata
-----------------

Once set, the custom metadata can be modified in the following manner:

.. image:: /Images/s3cmdremoveheader.png

List buckets in an account
--------------------------

.. image:: /Images/s3cmdls.png

List objects in a bucket
------------------------

Objects in a bucket can be listed using **s3cmd ls** like is shown below:

.. image:: /Images/s3cmdlsobjects.png

If the bucket was, for example, used to store a hierarchy of folders and files, then you need the **--recursive** flag in order to see the contents of a bucket.

.. image:: /Images/s3cmdlsobjects2.png

Throwing buckets and objects away
---------------------------------

Throwing away an object:

.. code-block:: console

    s3cmd rm s3://mybucket/myobject

Throwing away a bucket and its contents:

.. code-block:: console

    s3cmd rm --force --recursive s3://mybucket
    s3cmd rb s3://mybucket

Where on the first line all objects are thrown away and on the second line the bucket itself is thrown away.

.. note:: **Important:** You can only delete an empty bucket.

Upload large files (>5GB)
-------------------------

For files > 5GB files need to be uploaded in parts. Below you can see how this works.
 
.. image:: /Images/s3cmdmultipart.png

Downloading the file works the same as a regular download.

.. code-block:: console

    s3cmd get s3://mybucket/myobject

Sync folders
------------

It is possible to sync folders with their contents to buckets and vice versa. The image below shows you how.

.. image:: /Images/s3cmdsync.png

Encryption
----------

It is possible to let **s3cmd** encrypt your data before uploading. For this to work you have to setup gpg and add the following lines to your **.s3cfg** file. 

.. code-block:: console

    gpg_command = /usr/bin/gpg
    gpg_decrypt = %(gpg_command)s -d --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
    gpg_encrypt = %(gpg_command)s -c --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s
    gpg_passphrase = <password>

To upload an encrypted file you have to do the following:

.. code-block:: console

    s3cmd put -e <file name> s3://mybucket/myobject

Here the **-e** flag enforces the encryption. For downloading nothing special has to be done, so downloading the encrypted object is done by:

.. code-block:: console

    s3cmd get s3://mybucket/myobject
