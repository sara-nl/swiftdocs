.. _cyberduck:

*********
Cyberduck
*********

In this page you will find documentation about the usage of Cyberduck. 

.. contents:: 
    :depth: 4

Cyberduck offers a GUI to connect to almost a gazillion different storage systems with equally many protocols to copy, put, get and delete files and folders.
It can also be used to connect to Openstack SWIFT.
Cyberduck can be downloaded from https://cyberduck.io/ and is available for MS Windows and Mac OSX. 

======
Config
======

V2 authentication
-----------------

Users having a local keystone account can use the keystone V2 authentication version. We have a pre-configured profile for you. You can download it from: :download:`surfswiftv2.cyberduckprofile <../../Scripts/cyberduck_profile/surfswiftv2.cyberduckprofile>`.

Windows users need to copy the file to %APPDATA%\\Cyberduck\\Profiles. Mac users need to copy it to ~/Library/Group Containers/G69SCX94XU.duck/Library/Application Support/. 

It is also possible to use the default **Swift** profile that comes with Cyberduck. 

For the pre-configured profile you only need to supply the **Tenant ID** and the **Access Key**. Here the **Tenant ID** is your project name and the **Access Key** is your user name. Creating a new bookmark, for example, works as follows:

.. image:: /Images/cyberduckv2.png
           :width: 650px

After this you are prompted for a password when you click on the bookmark.

.. image:: /Images/cyberduckv2_2.png
           :width: 650px

You can choose to save your password.

V3 authentication
-----------------

Users using their SURFsara Central User Administration (CUA) account need to use keystone V3 authentication. This does not come with cyberduck so therefore we have provided a pre-configured profile for you. You can download it from: :download:`surfswiftv3.cyberduckprofile <../../Scripts/cyberduck_profile/surfswiftv3.cyberduckprofile>`. 

For this profile you need to supply the **Project Name**, the **User Domain** and the **User Name**. For CUA users, the **User Domain** has to be set to **CuaUsers**. If you have a local account, then you can also use this profile, but **User Domain** has to be set to **Default**.

Creating a new bookmark, for example, works as follows:

.. image:: /Images/cyberduckv3.png
           :width: 650px

After this you are prompted for a password when you click on the bookmark.

.. image:: /Images/cyberduckv3_2.png
           :width: 650px

S3 authentication
-----------------

It is also possible to use your S3 credentials to connect Cyberduck to SWIFT. Also for this case we have prepared a pre-configured profile that can be downloaded from: :download:`surfs3.cyberduckprofile <../../Scripts/cyberduck_profile/surfs3.cyberduckprofile>`.

For the profile, you need to supply your EC2 credentials, the **Access Key** and the **Secret Key**. 

Creating a new bookmark, for example, works as follows:

.. image:: /Images/cyberducks3.png
           :width: 650px

After this you are prompted to supply the secret key when you click on the bookmark.

.. image:: /Images/cyberducks3_2.png
           :width: 650px


=====
Video
=====

The video below shows you how to set things up.

.. raw:: html

    <iframe width="1120" height="630" src="https://www.youtube.com/embed/Dk1-l6yROes" frameborder="0" allowfullscreen></iframe>

====
Duck
====

Cyberduck al has a commandline client, called duck. It is available on MS Windows, Mac OSX and Linux. Information on how to install it is available at: https://trac.cyberduck.io/wiki/help/en/howto/cli. 

Information on how to use it is obtained by:

.. code-block:: bash

    duck --help

You need to install de profile :download:`surfswiftv3.cyberduckprofile <../../Scripts/cyberduck_profile/surfswiftv3.cyberduckprofile>` in ~/.duck/profiles.

Getting a listing of a container is done in the following manner:

.. code-block:: bash

    duck --username <project name:DOMAIN:user name> --password <password> -q -l surfswift://proxy.swift.surfsara.nl:5000/<container>

Users using keystone together with their SURFsara Central User Adminitration (CUA) account need to specify **CuaUsers** as **DOMAIN**. Users using local keystone account need to specify **default** as **DOMAIN**.
