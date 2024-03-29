.. _s5cmd:

***************************
S3 commandline client s5cmd
***************************

In this page you will find documentation about an S3 client. Here we refer to **buckets**, this is the S3 term for **containers**. They are identical.

.. contents::
    :depth: 4


=====
s5cmd
=====

The tool **s5cmd** allows you to parallelise workloads like data transfers. This is very convenient when you want to copy a whole directory with its contents to an S3 bucket or vice versa. More information may be found at https://github.com/peak/s5cmd, https://joshua-robinson.medium.com/s5cmd-for-high-performance-object-storage-7071352cc09d and https://aws.amazon.com/blogs/opensource/parallelizing-s2-workloads-s5cmd/. 

The key benefit of **s5cmd** is its greatly improved performance as compared to s3cmd and aws cli etc. 

Installation
------------

Binaries can be downloaded from: https://github.com/peak/s5cmd/releases for Windows, Mac and Linux.

For Openstack SWIFT, please use version 2.2.2 or above.

Authentication
--------------

In order to authenticate you need the same as for the :ref:`awscli <awscli>` client. See: http://doc.swift.surfsara.nl/en/latest/Pages/Clients/awscli.html#configuration.


Upload/Download an object to/from a bucket
------------------------------------------

First you need to setup the endpoint of the service as an environment variable:

.. code-block:: console

    export S3_ENDPOINT_URL=https://proxy.swift.surfsara.nl

An object can be uploaded to a bucket by the following command:

.. code-block:: console

    s5cmd cp <file name> s3://mybucket/myobject

It can be downloaded by:

.. code-block:: console

    s5cmd cp s3://mybucket/myobject <filename>


Upload a folder with contents to a bucket
-----------------------------------------

.. code-block:: console

    s5cmd cp /path/to/my/folder s3://mybucket

Download a bucket with contents to a directory
----------------------------------------------

.. code-block:: console

    s5cmd cp s3://mybucket/* /path/to/my/folder/.


Large files
-----------

.. note:: **Important:** By default **s5cmd** spawns 256 workers to do its tasks in parallel. This tool is really well suited for transferring a large number of small files. For larger files (>= 1GB) we have found it beneficial to reduce the number of workers to a smaller number, like for example 20, in order to reduce the load on the client side. To do that use the commandline flag :literal:`--numworkers <value>`. An example is shown below:

.. code-block:: console

    s5cmd --numworkers 20 cp /path/to/my/folder/with/big/files s3://mybucket
