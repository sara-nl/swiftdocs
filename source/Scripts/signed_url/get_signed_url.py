from __future__ import print_function

import sys
import argparse
import datetime
import hashlib
import hmac
import requests
from requests.utils import quote

# fill in the access and secret keys
access_key = ''
secret_key = ''

# request elements
region = 'NL'
endpoint = 'proxy.swift.surfsara.nl'
host = endpoint
endpoint = 'https://' + host

def encode(x):
# Check for encoding if we have python2 or python3
    if sys.version_info >= (3,0):
        return x.encode('utf-8')
    else:
        return x

# hashing methods
def hash(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

def createSignatureKey(key, datestamp, region, service):
    keyDate = hash(('AWS4' + key).encode('utf-8'), datestamp)
    keyRegion = hash(keyDate, region)
    keyService = hash(keyRegion, service)
    keySigning = hash(keyService, 'aws4_request')
    return keySigning

def hex_hash(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).hexdigest()

def createHexSignatureKey(key, datestamp, region, service):
    keyDate = hex_hash(encode('AWS4' + key), datestamp)
    keyRegion = hex_hash(encode(keyDate), region)
    keyService = hex_hash(encode(keyRegion), service)
    keySigning = hex_hash(encode(keyService), 'aws4_request')
    return keySigning

def expire_seconds(x):
# Check if supplied number of expiration seconds is a valid number
    x=int(x)
    if x<0:
        raise argparse.ArgumentTypeError("Expiration period must be a positive number of seconds")
    return x

# Parse command line arguments
parser=argparse.ArgumentParser(description='Create a signed s3 url.')
parser.add_argument('-b','--bucket',required=True,
                    help='supply bucket name')
parser.add_argument('-o','--object',required=True,
                    help='supply object name')
parser.add_argument('-m','--method',required=True,
                    choices=['put','get'],
                    help='supply http method')
parser.add_argument('-e','--expiration',required=False,
                    default=86400,type=expire_seconds,
                    help='supply expiration in seconds')

args=vars(parser.parse_args())

bucket=args['bucket']
object_key=args['object']
if args['method']=='get':
    http_method='GET'
else:
    http_method='PUT'
expiration=args['expiration']

# Assemble the request
time = datetime.datetime.utcnow()
timestamp = time.strftime('%Y%m%dT%H%M%SZ')
datestamp = time.strftime('%Y%m%d')

standardized_querystring = ( 'X-Amz-Algorithm=AWS4-HMAC-SHA256' +
                             '&X-Amz-Credential=' + access_key + '/' + datestamp + '/' + region + '/s3/aws4_request' +
                             '&X-Amz-Date=' + timestamp +
                             '&X-Amz-Expires=' + str(expiration) +
                             '&X-Amz-SignedHeaders=host' )
standardized_querystring_url_encoded = quote(standardized_querystring, safe='&=')

standardized_resource = '/' + bucket + '/' + object_key
standardized_resource_url_encoded = quote(standardized_resource, safe='&')

payload_hash = 'UNSIGNED-PAYLOAD'
standardized_headers = 'host:' + host
signed_headers = 'host'

standardized_request = (http_method + '\n' +
                        standardized_resource + '\n' +
                        standardized_querystring_url_encoded + '\n' +
                        standardized_headers + '\n' +
                        '\n' +
                        signed_headers + '\n' +
                        payload_hash)

# Assemble string-to-sign
hashing_algorithm = 'AWS4-HMAC-SHA256'
credential_scope = datestamp + '/' + region + '/' + 's3' + '/' + 'aws4_request'
sts = ( hashing_algorithm + '\n' +
        timestamp + '\n' +
        credential_scope + '\n' +
        hashlib.sha256(encode(standardized_request)).hexdigest() )

# Generate the signature
signature_key = createSignatureKey(secret_key, datestamp, region, 's3')
signature = hmac.new(signature_key,
                     (sts).encode('utf-8'),
                     hashlib.sha256).hexdigest()

# Create and send the request
# The 'requests' package autmatically adds the required 'host' header
request_url = ( endpoint + '/' +
                bucket + '/' +
                object_key + '?' +
                standardized_querystring_url_encoded +
                '&X-Amz-Signature=' +
                signature )

if http_method=='GET':
    request = requests.get(request_url)
else:
    request = requests.put(request_url)

signature_key_hex = createHexSignatureKey(secret_key, datestamp, region, 's3')

print ('pre-signed url: %s' % request_url) 
