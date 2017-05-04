.. _pythonlibrary:

**************
Python Library
**************

In this page you will find documentation about the python **swiftclient** library you can use to access swift.

.. contents:: 
    :depth: 4

=====================
Library documentation
=====================

There are numerous libraries and bindings for OpenStack SWIFT. These are listed on: https://docs.openstack.org/developer/swift/associated_projects.html. 

The only one that is officially supported by OpenStack is the `Python-SwiftClient`_. So this is the only one we will discuss here.
The `Python-SwiftClient`_ has a `Service API`_ and a `Connection API`_.


===========
Service API
===========

A higher-level API aimed at allowing developers an easy way to perform multiple operations asynchronously using a configurable thread pool. Documentation for each service method call can be found here: `swiftclient.service`_.

More detailed information on this API is described at the `Service API`_ page.
There are also examples given on that page. To let your scripts do the authentication you need to set some environment variables. That is also described on the `Service API`_ page.

One example of **stat** is given below:

First you need to set some environment variables for the authentication:

.. image:: /Images/stat_service_api_auth.png

Having done this you can run your script to do a **stat** on an object in a container.

.. image:: /Images/stat_service_api.png

==============
Connection API
==============

A low level API that provides methods for authentication and methods that correspond to the individual REST API calls described in the swift documentation.

For usage details see the client docs: `swiftclient.client`_.

A more detailed description and examples of the API is at the `Connection API`_ page. 

One example of **stat** is given below:

The script looks like this:

.. image:: /Images/stat_connection_api_script.png

Running this, you would get:

.. image:: /Images/stat_connection_api.png

.. Links:

.. _`Python-SwiftClient`: https://pypi.python.org/pypi/python-swiftclient
.. _`Service API`: https://docs.openstack.org/developer/python-swiftclient/service-api.html
.. _`Connection API`: https://docs.openstack.org/developer/python-swiftclient/client-api.html
.. _`swiftclient.service`: https://docs.openstack.org/developer/python-swiftclient/swiftclient.html#module-swiftclient.service
.. _`swiftclient.client`: https://docs.openstack.org/developer/python-swiftclient/swiftclient.html#module-swiftclient.client
