#!/bin/sh

# For CUA users fill in "CuaUsers" here. For local user fill in "Default"
export OS_PROJECT_DOMAIN_NAME=
# For CUA users fill in "CuaUsers" here. For local user fill in "Default"
export OS_USER_DOMAIN_NAME=

export OS_PROJECT_NAME=
export OS_USERNAME=
export OS_PASSWORD=
export OS_AUTH_URL=https://proxy.swift.surfsara.nl:5000/v3

JSONFILE=`mktemp`
chmod 600 ${JSONFILE}

TMPFILE=`mktemp`
chmod 600 ${TMPFILE}

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
