#!/bin/bash

#
# Copyright [2021] [Ron Trompert]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

MAXKEYS=1000

usage() {
    echo "versions_listing.sh \"bucket name\" [\"object name\"]" >&2
}

if [ $# -gt 2 -o $# -lt 1 ]; then
    usage
    exit 1
fi

bucket_name=$1

key=""
if [ $# -eq 2 ]; then
    key=$2
fi

# Check is bucket exists and has versionign enabled
error_log=`mktemp`
output=`mktemp`
retval=`aws s3api get-bucket-versioning --bucket ${bucket_name} 2>${error_log} 1>${output}; echo $?`
if [ ${retval} -ne 0 ]; then
    cat ${error_log} >&2
    rm -f ${error_log} ${output}
    exit 1
fi
enabled=`cat ${output} | jq -r '.Status'`
if [ "${enabled}" != "Enabled" ]; then
    echo ${bucket_name}" does not have versioning enabled" >&2
    rm -f ${error_log} ${output}
    exit 1
fi
rm -f ${error_log} ${output}

TMPFILE=`mktemp`

nexttoken=""

until [ "$nexttoken" == "null" ]
do
    if [ -z "$nexttoken" ]; then
        startingtoken=""
    else
        startingtoken="--starting-token ${nexttoken}"
    fi

    aws s3api list-object-versions ${startingtoken} --max-items ${MAXKEYS} --bucket ${bucket_name} >${TMPFILE}

    nexttoken=`cat ${TMPFILE} | jq -r '.NextToken'`

    if [ -z ${key} ];then
        cat ${TMPFILE} | jq -r '.Versions[] | .Key+";"+.VersionId+";"+.LastModified+";"+(.IsLatest|tostring)'
    else
        cat ${TMPFILE} | jq -r --arg key "$key" '.Versions[] | select(.Key==$key) .Key+";"+.VersionId+";"+.LastModified+";"+(.IsLatest|tostring)'
    fi
    if [ -z ${key} ];then
        cat ${TMPFILE} | jq -r '.DeleteMarkers[] | .Key+";"+.VersionId+";"+.LastModified+";"+(.IsLatest|tostring)+";delete_marker"'
    else
        cat ${TMPFILE} | jq -r --arg key "$key" '.DeleteMarkers[] | select(.Key==$key) .Key+";"+.VersionId+";"+.LastModified+";"+(.IsLatest|tostring)delete_marker'
    fi

done

rm -f ${TMPFILE}
