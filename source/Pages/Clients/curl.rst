.. _curl:

****
Curl
****

In this page you will find documentation about how to access SWIFT through curl.

.. contents:: 
    :depth: 4

=====
Usage
=====

Here we refer to the man pages of **curl**. But we do like to point out the following options:

:manpage:`curl(1)`

-i	Include the HTTP-header in the output. The HTTP-header includes things like server-name, date of the document, HTTP-version  and more...
-s	Silent or quiet mode. Don't show progress meter  or  error  messages.   Makes  curl mute. It will still output the data you ask for, potentially even to the terminal/stdout unless you redirect it.
-S	When used with -s, it makes curl show an error message if it fails.


==============
Authentication
==============


First you need to get a token that is valid for 24 hours that can be used instead of user name and password. Authentication is done through keystone. There are two versions supported, V2.0 and V3. Using V2.0, a token is created in the following manner:

.. image:: /Images/v2auth.png

Here the **json_pp** is just for the pretty print of the JSON output.

If you look at "token", you see the "id" which is your token and "expires" gives you the time when the token will expire. In the "serviceCatalog" at the "endpoints" of the "type: object-store", you see the "publicURL". This is the <storage url> you will need later on.

V3 authentication works a bit different. Here the token is returned in the http header. The script below should give you the right information:

.. code-block:: bash

    #!/bin/sh

    TMPFILE=`mktemp`
    chmod 600 ${TMPFILE}

    curl -i \
      -H "Content-Type: application/json" \
      -o ${TMPFILE} \
      -d '
    { "auth": {
        "identity": {
          "methods": ["password"],
          "password": {
            "user": {
              "name": "<user name>",
              "domain": { "id": "default" },
              "password": "<password>"
            }
          }
        }
      }
    }' \
     https://proxy.swift.surfsara.nl:5000/v3/auth/tokens

    echo
    cat ${TMPFILE} | grep 'X-Subject-Token:'

    echo
    tail -1 ${TMPFILE} | json_pp
    rm -f ${TMPFILE}

An example of the outut this script generates is below:

.. code-block:: console

    X-Subject-Token: gAAAAABZFbvo0zph96oF8E8J2oyndXFS9tNfxVFi9MSxpO7-hWL99_7Z7UTi_YlRLk1VHAosqZJpFoAvY62mJuRU6Z1S0tSqBP9I3MrVQeNNZDcLpCbyxIpbjsywM0KHm7kHeG_7AXKU6fMP13RbrUdU9cfHfSSWs_tZC-uSgfKbYBp7au8EJmM

    {
       "token" : {
          "issued_at" : "2017-05-12T13:43:04.000000Z",
          "project" : {
             "id" : "05b2aafab5a745eab2726d88649d95fe",
             "name" : "<project name>",
             "domain" : {
                "id" : "default",
                "name" : "Default"
             }
          },
          "expires_at" : "2017-05-12T14:43:04.000000Z",
          "methods" : [
             "password"
          ],
          "user" : {
             "domain" : {
                "id" : "default",
                "name" : "Default"
             },
             "id" : "bd4a4a9ea29344ccb828ab4a818e8576",
             "name" : "<user name>",
             "password_expires_at" : null
          },
          "roles" : [
             {
                "id" : "3c126a7986f04f9ebf2a27f083b8ffde",
                "name" : "admin"
             }
          ],
          "is_domain" : false,
          "audit_ids" : [
             "DMMZHCIPRo6rQ6qI6p_jVA"
          ],
          "catalog" : [
             {
                "endpoints" : [
                   {
                      "url" : "https://proxy.swift.surfsara.nl:35357/v3/",
                      "region_id" : "RegionOne",
                      "region" : "RegionOne",
                      "interface" : "admin",
                      "id" : "02a84a77a5534c0899ddb923eff58fd4"
                   },
                   {
                      "region" : "RegionOne",
                      "interface" : "public",
                      "id" : "b6c4d54a4e7a455f800cabfa68ebb941",
                      "region_id" : "RegionOne",
                      "url" : "https://proxy.swift.surfsara.nl:5000/v3/"
                   },
                   {
                      "region_id" : "RegionOne",
                      "url" : "https://proxy.swift.surfsara.nl:5000/v3/",
                      "interface" : "internal",
                      "region" : "RegionOne",
                      "id" : "f386325000a0458badb40c81f92f33ca"
                   }
                ],
                "id" : "9c3fe3a4a5f5409abf48513c72c5fa48",
                "name" : "keystone",
                "type" : "identity"
             },
             {
                "endpoints" : [
                   {
                      "id" : "2e0acde93b2d4989a7a08a5b15f2e7f7",
                      "interface" : "admin",
                      "region" : "RegionOne",
                      "region_id" : "RegionOne",
                      "url" : "https://proxy.swift.surfsara.nl/v1"
                   },
                   {
                      "region" : "RegionOne",
                      "interface" : "internal",
                      "id" : "c91a92ab40f7456894ecdce931fd655f",
                      "region_id" : "RegionOne",
                      "url" : "https://proxy.swift.surfsara.nl/v1/KEY_05b2aafab5a745eab2726d88649d95fe"
                   },
                   {
                      "interface" : "public",
                      "region" : "RegionOne",
                      "id" : "d1dfdf1eaf2e4092afe271afcfd2d998",
                      "url" : "https://proxy.swift.surfsara.nl/v1/KEY_05b2aafab5a745eab2726d88649d95fe",
                      "region_id" : "RegionOne"
                   }
                ],
                "type" : "object-store",
                "name" : "swift",
                "id" : "fd2cc7f02b6a4d389ef61ed2dc5a3362"
             }
          ]
       }
    }

The line with "X-Subject-Token:" gives you the token. In the JSON output you will find the token expiration time,"expires at". In the "catalog" section at the "endpoints" of "type" : "object-store" and "name" : "swift", you have to look for the "interface" : "public" and there you find the <storage url> "url" : "https://proxy.swift.surfsara.nl/v1/KEY_05b2aafab5a745eab2726d88649d95fe".

For users using keystone and their SURFsara Central User Administration account can use the following script:

.. code-block:: bash

    #!/bin/sh

    TMPFILE=`mktemp`
    chmod 600 ${TMPFILE}

    curl -i \
      -H "Content-Type: application/json" \
      -o ${TMPFILE} \
      -d '
    { "auth": {
        "identity": {
          "methods": ["password"],
          "password": {
            "user": {
              "name": "<user name>",
              "domain": { "name": "CuaUsers" },
              "password": "<password>"
            }
          }
        }
      }
    }' \
     https://proxy.swift.surfsara.nl:5000/v3/auth/tokens

    echo
    cat ${TMPFILE} | grep 'X-Subject-Token:'

    echo
    tail -1 ${TMPFILE} | json_pp
    rm -f ${TMPFILE}

The script below gives you just the token and the storage url using V3 authentication:

.. code-block:: bash

    #!/bin/sh

    TMPFILE=`mktemp`
    chmod 600 ${TMPFILE}

    PYTHONSCRIPT=`mktemp`

    if [ -f ${HOME}/.swiftrc ]; then
        . ${HOME}/.swiftrc
    fi

    input="OK"
    if [ -z ${OS_USERNAME} ]; then
        >&2 echo "Environment variable OS_USERNAME not set"
        input="NOTOK"
    fi
    if [ -z ${OS_PASSWORD} ]; then
        >&2 echo "Environment variable OS_PASSWORD not set"
        input="NOTOK"
    fi
    if [ -z ${OS_AUTH_URL} ]; then
        >&2 echo "Environment variable OS_AUTH_URL not set"
        input="NOTOK"
    fi
    if [ "${input}" = "NOTOK" ]; then
        exit 1
    fi


    cat > ${PYTHONSCRIPT} << EOF
    #!/usr/bin/env python
    import sys, json, re
    list=json.load(sys.stdin)["token"]["catalog"]
    for i in list:
        if i["type"]=="object-store" and re.search('swift',i["name"])!=None:
            for j in i["endpoints"]:
                if j["interface"]=="public":
                    print "export OS_STORAGE_URL="+j["url"]
    EOF
    chmod 755 ${PYTHONSCRIPT}

    JSONFILE=`mktemp`
    chmod 600 ${JSONFILE}

    cat >${JSONFILE} <<EOF
    { "auth": {
        "identity": {
          "methods": ["password"],
          "password": {
            "user": {
              "name": "${OS_USERNAME}",
              "domain": { "id": "default" },
              "password": "${OS_PASSWORD}"
            }
          }
        }
      }
    }
    EOF


    curl -i  \
      -H "Content-Type: application/json" \
      -o ${TMPFILE} \
      -d @${JSONFILE} \
     ${OS_AUTH_URL}/auth/tokens 2>/dev/null

    echo
    token=`cat ${TMPFILE} | grep 'X-Subject-Token:' | awk '{print $2}'`
    echo "export OS_AUTH_TOKEN="${token}

    echo
    tail -1 ${TMPFILE} | ${PYTHONSCRIPT}
    rm -f ${TMPFILE} ${PYTHONSCRIPT} ${JSONFILE}

Now you can run curl commands using:

.. code-block:: console

    curl -i -H "X-Auth-Token: <token>" ...

==================
Create a container
==================

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: <token>" <storage url>/mycontainer

===========================================
Upload/Download an object to/from container
===========================================

Uploading an object:

.. code-block:: console

    curl -i -T myobject -X PUT -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

Downloading an object:

.. code-block:: console

    curl -s -S -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject -O

================
Getting metadata
================

Information about containers can be obtained by:

.. code-block:: console

    curl -i --head -H "X-Auth-Token: <token>" <storage url>/mycontainer


Information about an object can be retrieved through:

.. code-block:: console

    curl -i --head -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

=================================
List the containers of an account
=================================

.. code-block:: console

    curl -s -S -X GET -H "X-Auth-Token: <token>" <storage url>

================================
List the contents of a container
================================

.. code-block:: console

    curl -s -S -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer

==================
Delete a container
==================

.. code-block:: console

    curl -s -S -X DELETE -H "X-Auth-Token: <token>" <storage url>/mycontainer

.. note:: **Important:** You can only delete an empty container. If you try to delete a non empty container, then you get the error message: "There was a conflict when trying to complete your request."

================
Delete an object
================

.. code-block:: console

    curl -s -S -X DELETE -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

========================================================
Set and get your own metadata for containers and objects
========================================================

For containers we have:

.. code-block:: console

    curl -s -S -X POST -H "X-Auth-Token: <token>" -H "X-Container-Meta-mymetadata: mystuff" <storage url>/mycontainer

.. note:: **Important:** The header which denotes the metadata item has to be of the form *X-Container-Meta-<name>* for containers.

For objects we have:

.. code-block:: console

    curl -s -S -X POST -H "X-Auth-Token: <token>" -H "X-Object-Meta-mymetadata: mystuff" <storage url>/mycontainer/myobject

.. note:: **Important:** The header which denotes the metadata item has to be of the form *X-Object-Meta-<name>* for objects.

Get the metadata for containers:

.. code-block:: console

    curl -s -S --head -H "X-Auth-Token: <token>" <storage url>/mycontainer

which lists only the metadata. Or:

.. code-block:: console

    curl -i -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer

which shows container metadata and lists objects. 

Get the metadata for objects:

.. code-block:: console

    curl -s -S --head -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

which lists only the metadata. Or:

.. code-block:: console

    curl -i -X GET -H "X-Auth-Token: <token>" <storage url>/mycontainer/myobject

which shows container metadata and gets the object data.

============================
Uploading large files (>5GB)
============================

It is only possible to upload objects with the size of at most 5GB in one go to SWIFT. It is possible to up and download larger objects. For this we refer to the documentation on large objects at: https://docs.openstack.org/developer/swift/overview_large_objects.html. 

There are dynamic large objects and static large objects. 
 - **Static Large Object** - Relies on a user provided manifest file. Advantageous for use cases when the developer wants to “mashup” objects from multiple containers and reference them in a self-generated manifest file. This gives you immediate access to the concatenated object after the manifest is accepted. Uploading segments into separate containers provides the opportunity for improved concurrent upload speeds. On the downside, the concatenated object’s definition is frozen until the manifest is replaced.
 - **Dynamic Large Object** - Relies on a container-listing zero-byte manifest file. Advantageous for use cases when the developer might add/remove segments from the manifest (e.g. objects from the container) at any time. A few disadvantages include reliance on eventual consistent container listings which means there may be some delay before access to the full concatenated object is available. There is also a requirement for all segments to be in a single container, which can limit concurrent upload speeds.

This page: https://docs.openstack.org/developer/swift/api/large_objects.html#comparison-of-static-and-dynamic-large-objects gives an overview of the difference between dynamic large objects and static large objects.

Dynamic Large Objects
---------------------

Suppose we have a 100MB file, called **file**,  that is uploaded in three chunks or segments.
Create a container for the big file:

.. code-block:: console

    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer

Split the big file into 40MB chunks

.. code-block:: console

    split -b 40000 file

The file is now split up in three files called **xaa**, **xab**, **xac**. Upload the three chunks to the segments container:

.. code-block:: console

    -rw-r--r-- 1 ron ron 100000000 apr 24 18:21 file
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xaa
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xab
    -rw-r--r-- 1 ron ron  20000000 apr 24 18:39 xac

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: ${<token>}" ${<storage url>}/mybigfilescontainer/file/001 --data-binary @xaa
    curl -i -X PUT -H "X-Auth-Token: ${<token>}" ${<storage url>}/mybigfilescontainer/file/002 --data-binary @xab
    curl -i -X PUT -H "X-Auth-Token: ${<token>}" ${<storage url>}/mybigfilescontainer/file/003 --data-binary @xac

Upload the manifest file:

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: ${<token>}" -H 'X-Object-Manifest: mybigfilescontainer/file/' ${<storage url>}/mybigfilescontainer/file --data-binary ''

Now you can download the file normally.

Static Large Objects
--------------------

Suppose we have a 100MB file, called **file**,  that is uploaded in three chunks.
Create a container for the big file and a separate container for the segments:

.. code-block:: console

    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer
    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments

Split the big file into 40MB chunks

.. code-block:: console

    split -b 40000 file

The file is now split up in three files called **xaa**, **xab**, **xac**. Upload the three chunks to the segments container:

.. code-block:: console

    -rw-r--r-- 1 ron ron 100000000 apr 24 18:21 file
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xaa
    -rw-r--r-- 1 ron ron  40000000 apr 24 18:39 xab
    -rw-r--r-- 1 ron ron  20000000 apr 24 18:39 xac

Upload the three segments to the segments container:

.. code-block:: console

    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments/xaa --data-binary @xaa
    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments/xab --data-binary @xab
    curl -i -X PUT -H "x-auth-token: ${<token>}" ${<storage url>}/mybigfilescontainer_segments/xac --data-binary @xac

Create the manifest file:

.. code-block:: bash

    MANIFEST="["

    for sp in /mybigfilescontainer_segments/xaa /mybigfilescontainer_segments/xab /mybigfilescontainer_segments/xac; do

        ETAG=$(curl -I -s -H "X-Auth-Token: ${<token>}" "${<storage url>}$sp" | perl -ane '/Etag:/ and print $F[1];');
        SIZE=$(curl -I -s -H "X-Auth-Token: ${<token>}" "${<storage url>}$sp" | perl -ane '/Content-Length:/ and print $F[1];');
        SEGMENT="{\"path\":\"$sp\",\"etag\":\"$ETAG\",\"size_bytes\":$SIZE}";
        [ "$MANIFEST" != "[" ] && MANIFEST="$MANIFEST,";   MANIFEST="$MANIFEST$SEGMENT";

    done
    
    MANIFEST="${MANIFEST}]"

This generates a manifest file like this:

.. code-block:: console

    [{"path":"/mybigfilescontainer_segments/xaa",
      "etag":"48e9a108a3ec623652e7988af2f88867",
      "size_bytes":40000000},
     {"path":"/mybigfilescontainer_segments/xab",
      "etag":"48e9a108a3ec623652e7988af2f88867",
      "size_bytes":40000000},
     {"path":"/mybigfilescontainer_segments/xac",
      "etag":"10e4462c9d0b08e7f0b304c4fbfeafa3",
      "size_bytes":20000000}]

Then upload the manifest file like this:

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: ${<token>}" ${<storage url>}/mybigfilescontainer/file?multipart-manifest=put --data-binary "$MANIFEST"

After this you can download the file as normal.

The **ETag** of the whole file can be computed as:

.. code-block:: console

    echo -n 'etagoffirstsegmentetagofsecondsegmentetagofthirdsegment...' | md5sum

So in this case this would be:

.. image:: /Images/bigfilesmd5sum.png

Run the following command to throw away the file, the segments and the manifest file:
    
.. code-block:: console

    curl -i -X DELETE -H "X-Auth-Token: ${<token>}" ${<storage url>}/mybigfilescontainer/file?multipart-manifest=delete

==============
Copy an object
==============

.. code-block:: console

    curl -i -X COPY -H "X-Auth-Token: <token>" -H "Destination: anothercontainer/myobject" <storage url>/mycontainer/myobject

===============
Bulk operations
===============

You can upload a tarball which will be extracted by SWIFT.

.. image:: /Images/bulk_upload.png

It is possible to do a bulk deletion. First you create a text file with all the containers and objects to be deleted. After that everything goes as follows:

.. image:: /Images/bulk_deletion.png

=================
Object versioning
=================

You can store multiple versions of your content so that you can recover from unintended overwrites. Object versioning is an easy way to implement version control, which you can use with any type of content.

First you need to create a container to store older versions of the objects:

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: <token>" <storage url>/mycontainer_versions

Then create a container for the latest version of the objects and tell SWIFT where to store the older versions of the object:

.. code-block:: console

    curl -i -X PUT -H "X-Auth-Token: <token>" -H "X-Versions-Location: mycontainer_versions" <storage url>/mycontainer

If you upload an object to a container and after that, upload a newer version of an object to the same container. The older version of the object is placed an a separate container. In this case that container would be **maersk_versions** under a name like:

.. code-block:: console

    <hexadecimal length of object name><object name><timestamp>

If you throw the latest version of the object away, the second latest version of the object is placed back into the container.

Here below is an example:

.. image:: /Images/curl_object_versioning.png

====
ACLs
====

There are account ACLs and container ACLs. With account ACLs you can grant different levels of access to all containers in an account. More information on this can be found at: https://www.swiftstack.com/docs/cookbooks/swift_usage/account_acl.html

There are also container ACLs. Using container ACLs you grant different levels of access to individual containers. More information on this is available at: https://www.swiftstack.com/docs/cookbooks/swift_usage/container_acl.html.

=================
Object expiration
=================

You can set object to expire. This means that object will be automatically deleted after a certain period of time. More information on this may be found at: https://docs.openstack.org/user-guide/cli-swift-set-object-expiration.html. This web page holds information about the swift commandline client. But it is straight forward to set the X-Delete-At and X-Delete-After headers in a curl command.
