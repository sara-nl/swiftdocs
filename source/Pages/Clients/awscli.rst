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
s3api = 
     endpoint_url = https://proxy.swift.surfsara.nl

Don't forget to:

.. code-block:: console

    chmod 600 ~/.aws/config

Information on how to the **aswcli** may be found at: `s3`_ and `s3api`_.

.. Links:

.. _`s3`: https://docs.aws.amazon.com/cli/latest/reference/s3/index.html
.. _`s3api`: https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html
