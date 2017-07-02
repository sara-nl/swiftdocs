.. _curl-token:

*************************
Create a token using curl
*************************

First you need to get a token that is valid for 24 hours that can be used instead of user name and password. Authentication is done through keystone. There are two versions supported, V2.0 and V3. We will only describe version V3 here.

The script below should give you the right information:

.. code-block:: bash

    #!/bin/sh

    export OS_PROJECT_DOMAIN_NAME=<project domain>
    export OS_USER_DOMAIN_NAME=<user domain>
    export OS_PROJECT_NAME=<project name>
    export OS_USERNAME=<user name>
    export OS_PASSWORD=<password>
    export OS_AUTH_URL=https://proxy.swift.surfsara.nl:5000/v3

    TMPFILE=`mktemp`
    chmod 600 ${TMPFILE}

    JSONFILE=`mktemp`
    chmod 600 ${JSONFILE}

    cat >${JSONFILE} <<EOF
    {
      "auth": {
        "identity": {
           "methods": ["password"],
              "password": {
                 "user": {
                    "domain": {"name": "${OS_USER_DOMAIN_NAME}"},
                       "name": "${OS_USERNAME}",
                       "password": "${OS_PASSWORD}"
                 }
              }
           },
           "scope": {
              "project": {
                 "domain": {"name": "${OS_PROJECT_DOMAIN_NAME}"},
                    "name": "${OS_PROJECT_NAME}"
              }
           }
       }
    }
    EOF

    curl -si  \
      -H "Content-Type: application/json" \
      -o ${TMPFILE} \
      -d @${JSONFILE} \
    ${OS_AUTH_URL}/auth/tokens 2>/dev/null

    echo
    cat ${TMPFILE} | grep 'X-Subject-Token:'

    echo
    tail -1 ${TMPFILE} | json_pp

    rm -f ${TMPFILE} ${JSONFILE}

It can be downloaded from :download:`get_token_and_json.sh <../../Scripts/bash/get_token_and_json.sh>`. An example of the output this script generates is below:

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

For users using keystone with a local acount should set:

.. code-block:: bash

    export OS_USER_DOMAIN_NAME="Default"
    export OS_PROJECT_DOMAIN_NAME="Default"

Users using keystone in combination with the SURFsara Central User Administration (CUA) account should set:

.. code-block:: bash

    export OS_USER_DOMAIN_NAME="CuaUsers"
    export OS_PROJECT_DOMAIN_NAME="CuaUsers"

The script below gives you just the token and the storage url using V3 authentication:

.. code-block:: bash

    #!/bin/sh

    export OS_PROJECT_DOMAIN_NAME=<project domain>
    export OS_USER_DOMAIN_NAME=<user domain>
    export OS_PROJECT_NAME=<project name>
    export OS_USERNAME=<user name>
    export OS_PASSWORD=<password>
    export OS_AUTH_URL=https://proxy.swift.surfsara.nl:5000/v3

    TMPFILE=`mktemp`
    chmod 600 ${TMPFILE}

    JSONFILE=`mktemp`
    chmod 600 ${JSONFILE}

    cat >${JSONFILE} <<EOF
    {
      "auth": {
        "identity": {
           "methods": ["password"],
              "password": {
                 "user": {
                    "domain": {"name": "${OS_USER_DOMAIN_NAME}"},
                       "name": "${OS_USERNAME}",
                       "password": "${OS_PASSWORD}"
                 }
              }
           },
           "scope": {
              "project": {
                 "domain": {"name": "${OS_PROJECT_DOMAIN_NAME}"},
                    "name": "${OS_PROJECT_NAME}"
              }
           }
       }
    }
    EOF

    PYTHONSCRIPT=`mktemp`
    chmod 755 ${PYTHONSCRIPT}

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

    curl -si  \
      -H "Content-Type: application/json" \
      -o ${TMPFILE} \
      -d @${JSONFILE} \
    ${OS_AUTH_URL}/auth/tokens 2>/dev/null | grep 'X-Subject-Token:' | awk '{print $2}'

    echo
    token=`cat ${TMPFILE} | grep 'X-Subject-Token:' | awk '{print $2}'`
    echo "export OS_AUTH_TOKEN="${token}

    echo
    tail -1 ${TMPFILE} | ${PYTHONSCRIPT}
    rm -f ${TMPFILE} ${PYTHONSCRIPT} ${JSONFILE}

It can be downloaded from: :download:`get_token_and_storage_url.sh <../../Scripts/bash/get_token_and_storage_url.sh>`. Now you can run curl commands using:

.. code-block:: console

    curl -i -H "X-Auth-Token: <token>" ...
