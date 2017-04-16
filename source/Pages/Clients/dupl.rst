.. _dupl:

*********
Duplicity
*********

Duplicity backs directories by producing encrypted tar-format volumes and uploading them to a remote or local file server. Because duplicity uses librsync, the incremental archives are space efficient and only record the parts of files that have changed since the last backup. Because duplicity uses GnuPG to encrypt and/or sign these archives, they will be safe from spying and/or modification by the server.

A large number of remote storage servers are supported. Openstack SWIFT is one of them. 

More information on Duplicity may be found at the `Duplicity <http://duplicity.nongnu.org/>`_ website or at this `Ubuntu <https://help.ubuntu.com/community/DuplicityBackupHowto>`_ site.

.. contents:: 
    :depth: 4

=============
Authorisation
=============

Duplicity requires some environment variables to be set, see below:

.. code-block:: console

    export SWIFT_USERNAME="user name"
    export SWIFT_PASSWORD="password"
    export SWIFT_AUTHURL="https://proxy.swift.surfsara.nl/auth/v1.0"
    export SWIFT_AUTHVERSION="1"

=================
Automatic backups
=================

For information on how to do automatic backups with duplicity, we refer to: https://www.digitalocean.com/community/tutorials/how-to-use-duplicity-with-gpg-to-securely-automate-backups-on-ubuntu.
