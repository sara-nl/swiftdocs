#!/bin/sh

# For CUA users fill in "CuaUsers" here. For local user fill in "Default"
export OS_PROJECT_DOMAIN_NAME=
# For CUA users fill in "CuaUsers" here. For local user fill in "Default"
export OS_USER_DOMAIN_NAME=

export OS_PROJECT_NAME=
export OS_USERNAME=
export OS_PASSWORD=
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
#!/usr/bin/python3
import sys, json, re
list=json.load(sys.stdin)["token"]["catalog"]
for i in list:
    if i["type"]=="object-store" and re.search('swift',i["name"])!=None:
        for j in i["endpoints"]:
            if j["interface"]=="public":
                print ("export OS_STORAGE_URL="+j["url"])
EOF

curl -si  \
  -H "Content-Type: application/json" \
  -o ${TMPFILE} \
  -d @${JSONFILE} \
 ${OS_AUTH_URL}/auth/tokens 2>/dev/null | grep -i 'X-Subject-Token:' | awk '{print $2}'
echo
token=`cat ${TMPFILE} | grep -i 'X-Subject-Token:' | awk '{print $2}'`
echo "export OS_AUTH_TOKEN="${token}

echo
tail -1 ${TMPFILE} | ${PYTHONSCRIPT}
rm -f ${TMPFILE} ${PYTHONSCRIPT} ${JSONFILE}
