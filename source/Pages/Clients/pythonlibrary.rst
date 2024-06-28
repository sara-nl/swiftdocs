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

==============
Connection API
==============

A low level API that provides methods for authentication and methods that correspond to the individual REST API calls described in the swift documentation. For usage details see the client docs: `swiftclient.client`_.
A more detailed description and examples of the API is at the `Connection API`_ page. 

One example of creating a new container is given below:

The script looks like this:

.. code-block:: bash

    #!/usr/bin/python3

    from swiftclient.client import Connection

    _authurl = 'https://proxy.swift.surfsara.nl:5000/v3'
    _auth_version = '3'
    _user = <user name>
    _project = <project name>
    _key = <password>

    #For local keystone accounts
    _user_domain='Default'
    _project_domain='Default'

    #For keystone accounts coupled to SURF CUA accounts
    #_user_domain='CuaUsers'
    #_project_domain='CuaUsers'

    _os_options = {
        'user_domain_name': _user_domain,
        'project_domain_name': _project_domain,
        'project_name': _project
    }

    conn = Connection(
        authurl=_authurl,
        user=_user,
        key=_key,
        os_options=_os_options,
        auth_version=_auth_version
    )

    #Create a container
    container_name = 'my-new-container'
    conn.put_container(container_name)

If you are a keystone user with a local account, then both the *project domain*  and *user domain* have the value **Default**. If you are a keystone user with a SURF Central User Administration (CUA) account, then both the *project domain* and *user domain* must be set to **CuaUsers**.

===========
Service API
===========

A higher-level API aimed at allowing developers an easy way to perform multiple operations asynchronously using a configurable thread pool. Documentation for each service method call can be found here: `swiftclient.service`_.

More detailed information on this API is described at the `Service API`_ page.
There are also examples given on that page. To let your scripts do the authentication you need to set some environment variables. That is also described on the `Service API`_ page.

One example of **stat** is given below:

First you need to set some environment variables for the authentication:

.. code-block:: bash

    export OS_PROJECT_DOMAIN_NAME=<project domain>
    export OS_USER_DOMAIN_NAME=<user domain>
    export OS_PROJECT_NAME=<project>
    export OS_USERNAME=<user>
    export OS_PASSWORD=<password>
    export OS_AUTH_URL=https://proxy.swift.surfsara.nl:5000/v3
    export OS_IDENTITY_API_VERSION=3
    export OS_AUTH_VERSION=3


Having done this you can run your script to do,for example, a **stat** on an object in a container. Such a script could look like this:

.. code-block:: bash

    #!/usr/bin/python3

    import logging
    import pprint

    from swiftclient.service import SwiftService
    from sys import argv

    logging.basicConfig(level=logging.ERROR)
    logging.getLogger("requests").setLevel(logging.CRITICAL)
    logging.getLogger("swiftclient").setLevel(logging.CRITICAL)
    logger = logging.getLogger(__name__)

    _opts = {'object_dd_threads': 20}
    with SwiftService(options=_opts) as swift:
        container = argv[1]
        objects = argv[2:]
        header_data = {}
        stats_it = swift.stat(container=container, objects=objects)
        for stat_res in stats_it:
            if stat_res['success']:
                header_data[stat_res['object']] = stat_res['headers']
            else:
                logger.error(
                    'Failed to retrieve stats for %s' % stat_res['object']
                )
        pprint.pprint(header_data)

If you are a keystone user with a local account, then both the *project domain*  and *user domain* have the value **Default**. If you are a keystone user with a SURF Central User Administration (CUA) account, then both the *project domain* and *user domain* must be set to **CuaUsers**.
Running this you could get something like this:

.. image:: /Images/pythonstat.png

.. Links:

.. _`Python-SwiftClient`: https://pypi.python.org/pypi/python-swiftclient
.. _`Service API`: https://docs.openstack.org/developer/python-swiftclient/service-api.html
.. _`Connection API`: https://docs.openstack.org/developer/python-swiftclient/client-api.html
.. _`swiftclient.service`: https://docs.openstack.org/developer/python-swiftclient/swiftclient.html#module-swiftclient.service
.. _`swiftclient.client`: https://docs.openstack.org/developer/python-swiftclient/swiftclient.html#module-swiftclient.client
