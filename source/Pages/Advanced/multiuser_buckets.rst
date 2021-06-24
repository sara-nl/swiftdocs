.. _multiuser_buckets:

*****************
Multiuser buckets
*****************

Consider the following usecase:

* There is a single Swift project
* There are multiple buckets/containers in the project
* Different users should have readonly, read-write or no access to the buckets
* The preferred way of accessing the buckets is using the S3 protocol

The first thing to realize is that a Swift project is not linked to a single user, but multiple users can have different levels of access to a project.

At this time we have two roles:

* swiftoperator (has full access)
* user (has no access unless explicitely granted)

If a user has a CUA account, SURF objectstore admins do not have to create them. If there is no CUA account, a local Swift acount will be created and the credentials will be provided.

Assigning users their role is done by the objectstore administrators.

A user with the 'operator' role can use ACLs to provide access to users with the 'user' role. Note that there are *Swift* ACLs, not S3 ACLs.

These ACLs work on the container level, users can have read-only or read-write access, also listings can be enabled or disabled. 

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

In the environment variables domains must be made explicit, since we are now mixing domains:
::
    export OS_PROJECT_DOMAIN_NAME=CuaUsers
    export OS_PROJECT_NAME="testproject"
    export OS_USER_DOMAIN_NAME=Default
    export OS_USERNAME=user1
    export OS_PASSWORD=password123
    export OS_AUTH_URL=https://proxy.swift.surfsara.nl:5000/v3
    export OS_IDENTITY_API_VERSION=3