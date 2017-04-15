.. _python-swift-client:

*******************
Python SWIFT client
*******************

In this page you will find documentation about the Python SWIFT client that are available.

.. contents:: 
    :depth: 4

=============
Authorisation
=============

.. image:: /Images/auth.jpg
           :width: 300px
           :height: 225px

The following environment variables are useful to set if you don't want them to provide them all the time on the command line.

.. code-block:: console

         export ST_AUTH=https://proxy.swift.surfsara.nl/auth/v1.0
         export ST_USER=<my user name>
         export ST_KEY=<my password>

==================
Create a container
==================
.. image:: /Images/make_container.png
           :width: 316px


A container can be created by the following command:
.. code-block:: console

         swift post mycontainer

===============================
Upload an object to a container
===============================
.. image:: /Images/upload.jpg
           :width: 300px


.. code-block:: console

         swift upload mycontainer myobject

If the container **mycontainer** does not exist yet, then it will be created.

.. Links:

.. _`SURFsara helpdesk`: https://www.surf.nl/en/about-surf/contact/helpdesk-surfsara-services/index.html

.. _`SURFsara application form`: https://e-infra.surfsara.nl/
