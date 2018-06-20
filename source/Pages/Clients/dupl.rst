.. _dupl:

*********
Duplicity
*********

Duplicity backs directories by producing encrypted tar-format volumes and uploading them to a remote or local file server. Because duplicity uses librsync, the incremental archives are space efficient and only record the parts of files that have changed since the last backup. Because duplicity uses GnuPG to encrypt and/or sign these archives, they will be safe from spying and/or modification by the server.

A large number of remote storage servers are supported. Openstack SWIFT is one of them. 

More information on Duplicity may be found at the `Duplicity <http://duplicity.nongnu.org/>`_ website or here: 

- https://help.ubuntu.com/community/DuplicityBackupHowto
- https://www.zetta.io/en/help/articles-tutorials/backup-linux-duply/
- https://raymii.org/s/tutorials/Encrypted_Duplicity_Backups_to_Openstack_Swift_Objectstore.html.

.. contents:: 
    :depth: 4

=============
Authorisation
=============

Duplicity requires some environment variables to be set, see below:

.. code-block:: console

    export SWIFT_USERNAME=<user name>
    export SWIFT_PASSWORD=<password>
    export SWIFT_AUTHURL="https://proxy.swift.surfsara.nl:5000/v3"
    export SWIFT_AUTHVERSION="3"
    export SWIFT_TENANTNAME=<project name>
    export SWIFT_USER_DOMAIN_NAME=<user domain name>
    export SWIFT_PROJECT_DOMAIN_NAME=<project domain name>

For keystone users with local account the *user domain name* and the *project domain name* is **Default**. For users using keystone coupled to their SURFsara Central User Administration (CUA) account, *user domain name* and *project domain name* must be set to **CuaUsers**.

=================
Automatic backups
=================

For information on how to do automatic backups with duplicity, we refer to: https://www.digitalocean.com/community/tutorials/how-to-use-duplicity-with-gpg-to-securely-automate-backups-on-ubuntu.
