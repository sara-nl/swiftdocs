.. _python-swift-client:

*******************
Python SWIFT client
*******************

In this page you will find documentation about the Python SWIFT client that are available.

.. contents:: 
    :depth: 4

============
Installation
============

This page will provide information on how to install the python swift client and how to use it. The page :ref:`Installation Instructions of the Python SWIFT Client on Linux <python-swift-client-linux>` tells you how to install the client on various flavours of Linux.

For windows it is rather similar. You can read about installation on windows at :ref:`Installation Instructions of the Python SWIFT Client on Windows <python-swift-client-windows>`

For information on how to install de swift command line client on Mac OSX, please, have a look at: :ref:`Installation Instructions of the Python SWIFT Client on OSX <python-swift-client-osx>`.

=====
Usage
=====

Now the usage of the **swift** commandline tools is like:

.. code-block:: console

         swift [options] <command> [--help] [<command options>]

More details and examples are provided below.

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

This holds for local keystone users. Users using their account in the SURF Central User Administration (CUA) through keystone need the specify the following:

.. code-block:: console

    export OS_PROJECT_DOMAIN_NAME=CuaUsers
    export OS_USER_DOMAIN_NAME=CuaUsers

for the **OS_PROJECT_DOMAIN_NAME** and **OS_USER_DOMAIN_NAME** environment variables. Apart from using your user name and password, it is also possible to generate a token that is valid for 24 hours. This may be handy if you are running the script elsewhere on a batch system and you don't want to send you username and password with your batch job. You can use this token to access your data in SWIFT.

Setting the environment variables as shown above holds for Linux and Mac OSX. For Windows you may want to have a look at: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.3

You can get a token in the following way:

.. image:: /Images/stat.png

What you need is the **StorageURL** and the **Auth Token**. You can use these two to run the swift commands for the next 24 hours without supplying your user name and password.

.. code-block:: console

         swift --os-auth-token <TOKEN> --os-storage-url <STORAGE URL> [options] <command> [--help] [<command options>]

For example:
        
.. image:: /Images/list.png

==================
Create a container
==================

.. image:: /Images/make_container.png
           :width: 600px


A container can be created by the following command:

.. code-block:: console

         swift post mycontainer

=============================================
Upload/Download an object to/from a container
=============================================

.. image:: /Images/upload.jpg
           :width: 600px


.. code-block:: console

         swift upload mycontainer myobject

If the container **mycontainer** does not exist yet, then it will be created. By default, the client will verify the checksum during the upload. Downloading an object from a container goes as follows:

.. code-block:: console

         swift download mycontainer myobject

Downloading the whole content of a container is done by:

.. code-block:: console

         swift download mycontainer


=================
Getting metadata
=================

.. image:: /Images/metadata.jpg
           :width: 600px

Container metadata can be obtained in the following manner:

.. image:: /Images/stat_container.png

**Bytes** is the total number of bytes of all object in the container, 
**Objects** is the number of objects in the container and 
**X-Storage-Policy** is the storage policy.

Object metadata can be obtained by the following command:

.. image:: /Images/stat_object.png

**Content Length** is the size in bytes and 
**ETag** is the md5 checksum of the object.

=================================
List the containers in an account
=================================

The containers in an account can be listed like:

.. code-block:: console

         swift list

============================
List contents of a container
============================

.. image:: /Images/contents-container.jpg
           :width: 600px

The objects in a container can be listed like:

.. code-block:: console

         swift list mycontainer

====================================
Throwing containers and objects away
====================================

.. image:: /Images/delete_container.png

Delete one object from a container:

.. code-block:: console

         swift delete mycontainer myobject


Delete a container with all objects in it:

.. code-block:: console

         swift delete mycontainer

================================================
Set your own metadata for containers and objects
================================================

To set metadata for an container goes in the following manner:

.. image:: /Images/metadata_container.png

Setting metadata for an object works in an identical fashion.

===============
Copying objects
===============

It is possible to copy objects. This goes as follows:

.. code-block:: console

    swift copy --destination /newcontainer/newobject oldcontainer oldobject

Also the object's metadata will be copied, unless you use the **\-\-fresh-metadata** flag. 


===============================
Renaming containers and objects
===============================

.. note:: **Important:** It is NOT possible to rename a container. This means that you have to think really well about naming containers before you upload a PB of data. 

It is possible to rename an object but not in the classical sense. First you need to copy an object using, for example, the method above and then throw the original object away.


============================
Uploading large files (>5GB)
============================

It is only possible to upload objects with the size of at most 5GB in one go to SWIFT. It is possible to up and download larger objects when the large object is uploaded in chunks. For the python SWIFT client you can upload an object larger than 5GB in the following way:

.. code-block:: console

    swift upload --use-slo -S <chunk size in bytes> mycontainer myobject

Here is an example:

.. image:: /Images/bigfiles.png

For downloading you can just proceed as usual. For more information on this we refer to the documentation on large objects at: https://docs.openstack.org/developer/swift/overview_large_objects.html. 

There are Dynamic Large Objects and Static Large Objects when it comes to large object uploads. The :ref:`curl <curl>` page has some information on this. Both type of objects have their use cases. Dynamic Large Objects may have issues with end to end integrity of data which Static Large Objects don't. Therefore we recommend to use the **\-\-use-slo** flag. 

=================
Object versioning
=================

You can store multiple versions of your content so that you can recover from unintended overwrites. Object versioning is an easy way to implement version control, which you can use with any type of content.

The first thing you have to do is create a container where old versions of objects are stored.

.. code-block:: console

    swift post maersk_versions

Then you have to create a container where to store the latest version of the objects and tell swift where to store the older versions:

.. code-block:: console

    swift post maersk -H "X-Versions-Location:maersk_versions"

If you upload an object to a container and after that, upload a newer version of an object to the same container. The older version of the object is placed an a separate container. In this case that container would be **maersk_versions** under a name like:

.. code-block:: console

    <hexadecimal length of object name><object name><timestamp>

If you throw the latest version of the object away, the second latest version of the object is placed back into the container.

Here below is an example:

.. image:: /Images/object_versioning.png

====
ACLs
====

You can set ACLs on containers. Using container ACLs you grant different levels of access to individual containers. More information on this is available at: https://docs.openstack.org/swift/latest/overview_acl.html.


=================
Object expiration
=================

You can set object to expire. This means that object will be automatically deleted after a certain period of time. More information on this may be found at: https://docs.openstack.org/swift/latest/api/object-expiration.html.

==============
Temporary URLs
==============

With the **TempURL** mechanism it is possible to provide temporary access to objects. This can be really useful if large objects need to be downloaded from SWIFT storage by a user that does not have public access.

First you have to set a secret key, which can just be any random string
you make up yourself:

.. code-block:: console

    swift post -m 'Temp-URL-Key: <some random string you make up yourself>'
    
This is a one-time action. You do not need to set a new key every time
you want to create a temporary URL for an object.

Then you create the **TempURL**.

.. code-block:: console

    swift tempurl <method> <seconds> <path> <key>

Here **method** may be PUT, GET, HEAD, POST and  DELETE and determines
what action someone can perform with the URL. To simply share an object
for download the GET action is what you want. 

The amount of seconds that the temporary URL is valid is given by **seconds**. 

The **path** value is the last part of the regular URL of the
object you want to make available. I.e. the part of the URL after the 
``https://proxy.swift.surfsara.nl`` hostname. See the example below for details.

Finally the **key** is the random secret key you have made up yourself 
in the first step.

An example of creating a temporary URL is shown below:

.. image:: /Images/tempurl.png

As the example shows the URL returned by the **swift tempurl** command
does not provide the complete URL. It needs to be prefixed with the
actual server URL part (``https://proxy.swift.surfsara.nl``). In case this 
server URL changes in future you can retrieve the current value with ``swift stat -v``
and look at the **StorageURL** field.

Note that the generated temporary URL contains fields (**temp_url_sig**
and *temp_url_expires**) that are checked against what is stored on 
the server. In this way someone cannot forge a URL to get unauthorized
access to files.

