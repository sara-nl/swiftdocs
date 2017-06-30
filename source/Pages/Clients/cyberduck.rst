.. _cyberduck:

*********
Cyberduck
*********

In this page you will find documentation about the usage of Cyberduck.

.. contents:: 
    :depth: 4

Cyberduck offers a GUI to connect to almost a gazillion different storage systems with equally many protocols to copy, put, get and delete files and folders.
It can also be used to connect to Openstack SWIFT.
Cyberduck can be downloaded from https://cyberduck.io/. 

======
Config
======

Users having a local keystone account can use the keystone V2 authentication version. This comes with cyberduck in the **Swift** profile. The configuration is given below:

.. code-block:: console

    Server: proxy.swift.surfsara.nl
    Port: 5000
    Tenant ID/Access Key: <ProjectName>:<Username>
    Secret Key: <YourPassword>

.. image:: /Images/cyberduckv2.png
           :width: 650px

Users using their SURFsara Central User Administration (CUA) account need to use keystone V3 authentication. This does not come with cyberduck so therefore we have provided it for you. You can download it from: :download:`surfswift cyberduck profile </Scripts/cyberduck_profile/surfswift.cyberduckprofile`. The configuration is given below:

.. code-block:: console

    Server: proxy.swift.surfsara.nl
    Port: 5000
    Project Name:User Domain:Username: <Project Name>:<User Domain>:<Username>
    Password: <YourPassword>

.. image:: /Images/cyberduckv3.png
           :width: 650px


=====
Video
=====

The video below shows you how to set things up.

.. raw:: html

    <iframe width="1120" height="630" src="https://www.youtube.com/embed/Dk1-l6yROes" frameborder="0" allowfullscreen></iframe>



