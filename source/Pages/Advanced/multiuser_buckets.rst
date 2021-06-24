.. _multiuser_buckets:

*****************
Multiuser buckets
*****************

.. contents::
    :depth: 2

Consider the following usecase:

* There is a single Swift project
* There are multiple buckets/containers in the project
* Different users should have readonly, read-write or no access to the buckets
* The preferred way of accessing the buckets is using the S3 protocol

Users and roles
***************

The first thing to realize is that a Swift project is not linked to a single user, but multiple users can have different levels of access to a project.

At this time we have two roles:

* swiftoperator (has full access)
* user (has no access unless explicitely granted)

If a user has a CUA account, SURF objectstore admins do not have to create them. If there is no CUA account, a local Swift acount will be created and the credentials will be provided.

Assigning users their role is done by the objectstore administrators.

A user with the 'operator' role can use ACLs to provide access to users with the 'user' role. Note that there are *Swift* ACLs, not S3 ACLs.

These ACLs work on the container level, users can have read-only or read/write access. 

In practice

Assuming we have a project:
::
    # openstack project show 75e0e9efc598123c98a339e871e819d1
    +-------------+----------------------------------+
    | Field       | Value                            |
    +-------------+----------------------------------+
    | description | Our testproject                  |
    | domain_id   | 57549dbccee745289c9d6967da211854 |
    | enabled     | True                             |
    | id          | 75e0e9efc598123c98a339e871e819b1 |
    | is_domain   | False                            |
    | name        | testproject                      |
    | options     | {}                               |
    | parent_id   | 58549dbccee745289c9d6967da211854 |
    | tags        | []                               |
    +-------------+----------------------------------+

Using a  CUA user a  swiftoperator:
::
    # openstack role assignment list --project 75e0e9efc598123c98a339e871e819b1 --names
    +---------------+-----------------+-------+-----------------+--------+--------+-----------+
    | Role          | User            | Group | Project         | Domain | System | Inherited |
    +---------------+-----------------+-------+-----------------+--------+--------+-----------+
    | swiftoperator | user1@CuaUsers  |       | user1@CuaUsers  |        |        | False     |
    +---------------+-----------------+-------+-----------------+--------+--------+-----------+

We also have a second, local,  keystone user:
::
   # openstack user show 237ab7ef9d9c473abe02bce488fe0818
   +---------------------+----------------------------------+
   | Field               | Value                            |
   +---------------------+----------------------------------+
   | default_project_id  | 45d98b770456d4bcbefeda0ae3dc1547 |
   | domain_id           | default                          |
   | email               | user2@surf.nl                    |
   | enabled             | True                             |
   | id                  | 237ab7ef9d9c473abe02bce488fe0818 |
   | name                | user2                            |
   | options             | {}                               |
   | password_expires_at | None                             |
   +---------------------+----------------------------------+
 
We can add this user a as swiftoperator to the project:
::
    # openstack role add --user 237ab7ef9d9c473abe02bce488fe0818 --project 57549dbccee745289c9d6967da211854 swiftoperator
.. note::  This needs to be done by a SURF admin.

This user now has full access to the project.
::
    # openstack role assignment list --project 75e0e9efc598489c98a339e871e819d1 --names
    +---------------+-----------------+-------+----------------------+--------+--------+-----------+
    | Role          | User            | Group | Project              | Domain | System | Inherited |
    +---------------+-----------------+-------+----------------------+--------+--------+-----------+
    | swiftoperator | user2@Default   |       | testproject@CuaUsers |        |        | False     |
    | swiftoperator | user1@CuaUsers  |       | testproject@CuaUsers |        |        | False     |
    +---------------+-----------------+-------+----------------------+--------+--------+-----------+


To revoke access for this user:
::
    # openstack role remove --user 237ab7ef9d9c473abe02bce488fe0818 --project 75e0e9efc598123c98a339e871e819b1 swiftoperator
.. note::  This needs to be done by a SURF admin.

In the environment variables domains must be made explicit, since we are now mixing domains:
::
    export OS_PROJECT_DOMAIN_NAME=CuaUsers
    export OS_PROJECT_NAME="testproject"
    export OS_USER_DOMAIN_NAME=Default
    export OS_USERNAME=user1
    export OS_PASSWORD=password123
    export OS_AUTH_URL=https://proxy.swift.surfsara.nl:5000/v3
    export OS_IDENTITY_API_VERSION=3

Adding a user with read-only access using ACLs
**********************************************

In some cases you may want to add a user that can read but not write. This can be done using Swift ACLs.
Note: Since we use the keystone auth system, we only support container ACLs, not account ACLs.

For our example we have a third user:
::
    # openstack user show user3
    +---------------------+----------------------------------+
    | Field               | Value                            |
    +---------------------+----------------------------------+
    | domain_id           | default                          |
    | email               | user3@domain.nl                  |
    | enabled             | True                             |
    | id                  | 63u34d5df62947f987fb54c119a81dd1 |
    | name                | user3                            |
    | options             | {}                               |
    | password_expires_at | None                             |
    +---------------------+----------------------------------+

We add the user to the project, with the 'user' role:
::
    # openstack role add --user 63u34d5df62947f987fb54c119a81dd1 --project 75e0e9efc598123c98a339e871e819b1 user
    # openstack role assignment list --names --project 75e0e9efc598123c98a339e871e819b1
    +---------------+-----------------+-------+----------------------+--------+--------+-----------+
    | Role          | User            | Group | Project              | Domain | System | Inherited |
    +---------------+-----------------+-------+----------------------+--------+--------+-----------+
    | swiftoperator | user1@CuaUsers  |       | testproject@CuaUsers |        |        | False     |
    | swiftoperator | user2@Default   |       | testproject@CuaUsers |        |        | False     |
    | user          | user3@Default   |       | testproject@CuaUsers |        |        | False     |
    +---------------+-----------------+-------+----------------------+--------+--------+-----------+
.. note::  This needs to be done by a SURF admin.

The user also needs the default project set to the project in question:
::
    # openstack user set --project 75e0e9efc598123c98a339e871e819b1 user3
.. note::  This needs to be done by a SURF admin.

At this point the user can't do anything, first the ACLs must be set. This can be done by a user with the 'swiftoperator' role.

If you want to give user3 read-only access to a bucket named 'readonly':
::
    $ swift post readonly --read-acl "*:63u34d5df62947f987fb54c119a81dd1"

Now, user3 can see a listing of the container and download objects:
::
    $ swift list readonly
    test.txt
    test2.txt
    $ swift download readonly test.txt
    test.txt [auth 0.333s, headers 0.535s, total 0.537s, 0.000 MB/s]

But they cannot upload:
::
    $ swift upload readonly test3.txt 
    Warning: failed to create container 'readonly': 403 Forbidden: Forbidden: This account requires a token granted by SwiftSta
    Object PUT failed: https://proxy.swift.surfsara.nl/v1/KEY_75e0e9efc598123c98a339e871e819b1/readonly/test3.txt 403 Forbidden [first 60 chars of response] Forbidden: This account requires a token granted by SwiftSta

Suppose the user should be able to upload into a container called 'readwrite':
::
    $ swift post readwrite --read-acl "*:63u34d5df62947f987fb54c119a81dd1"
    $ swift post readwrite --write-acl "*:63u34d5df62947f987fb54c119a81dd1"

The Swift client will show a warning that the container can't be created, but the upload succeeds:
::
    $ swift upload readwrite test3.txt
    Warning: failed to create container 'readwrite': 403 Forbidden: Forbidden: This account requires a token granted by SwiftSta
    test3.txt

The warning occurs because the client cannot 'see' that the container already exists.
This is because user3 can't see a listing of all containers. They can, however, see the contents of the containers they have access to.
::
    $ swift list
    Account GET failed: https://proxy.swift.surfsara.nl/v1/KEY_75e0e9efc598123c98a339e871e819b1?format=json 403 Forbidden [first 60 chars of response] Forbidden: This account requires a token granted by SwiftSta
    Failed Transaction ID: txbbb802e84e764c4f859a7-0060d4777f

    $ swift list readwrite
    test.txt
    test2.txt
    test3.txt

Doing this using the S3 protocol
********************************

When using S3 the ACLs are enforced in the same manner. In this example the aws-cli client is used with the S3 access and secret generated by user3:
::
    $ aws s3 ls s3://readwrite
    2021-06-24 14:17:37 16 test.txt
    2021-06-23 17:12:51 16 test2.txt

    $ aws s3 ls s3://readonly
    2021-06-23 17:12:36 16 test.txt
    2021-06-23 14:25:39 16 test2.txt

    $ aws s3 cp test.txt s3://readonly/test.txt
    upload failed: ./test.txt to s3://readonly/test.txt An error occurred (AccessDenied) when calling the PutObject operation: Access Denied.

    $ aws s3 cp test.txt s3://readwrite/test3.txt
    upload: ./test.txt to s3://readwrite/test3.txt 

    $ aws s3 ls s3://readwrite
    2021-06-24 14:17:37 16 test.txt
    2021-06-23 17:12:51 16 test2.txt
    2021-06-23 17:09:50 16 test3.txt