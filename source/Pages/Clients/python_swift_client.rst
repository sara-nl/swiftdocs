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

The following environment variables are usefull to set if you don't want them to provide them all the time on the command line.

----

.. image:: /Images/auth.jpg
           :align: right
           :width: 300px

.. code-block:: console

         export ST_AUTH=https://proxy.swift.surfsara.nl/auth/v1.0
         export ST_USER=<my user name>
         export ST_KEY=<my password>

----

==================
Create a container
==================

.. code-block:: console

         swift post mycontainer

.. Links:

.. _`SURFsara helpdesk`: https://www.surf.nl/en/about-surf/contact/helpdesk-surfsara-services/index.html

.. _`SURFsara application form`: https://e-infra.surfsara.nl/
