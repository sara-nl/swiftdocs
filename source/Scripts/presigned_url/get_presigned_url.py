#!/usr/bin/python3

import sys
import os
import re
import argparse
import textwrap
import configparser
import datetime
import hashlib
import hmac
import requests
from requests.utils import quote

default_config='~/.aws/config'
default_secrets='~/.aws/credentials'
host_regexp=re.compile('http[s]{0,1}://(.+)')


def encode(x):
    return x.encode('utf-8')

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

def get_config(config,profile):
    if not os.path.exists(config): return None,None
    cfgparser = configparser.RawConfigParser()
    cfgparser.read(config)
    if profile not in cfgparser.sections(): return None,None
    endpoint=cfgparser.get(profile,'endpoint_url')
    region=cfgparser.get(profile,'region')
    del cfgparser
    return endpoint,region

def get_secrets(secrets,profile):
    if not os.path.exists(secrets): return None,None
    cfgparser = configparser.RawConfigParser()
    cfgparser.read(secrets)
    if profile not in cfgparser.sections(): return None,None
    access_key=cfgparser.get(profile,'aws_access_key_id')
    secret_key=cfgparser.get(profile,'aws_secret_access_key')
    del cfgparser
    return access_key,secret_key

# Parse command line arguments
parser=argparse.ArgumentParser(description='Create a signed s3 url.',formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog=textwrap.dedent('''\
                This script uses the standard aws config and credentials file. 
                Setting the environment variables AWS_PROFILE, AWS_ACCESS_KEY_ID,
                AWS_SECRET_ACCESS_KEY, AWS_ENDPOINT_URL and AWS_REGION can also
                be used.'''))
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
parser.add_argument('-c','--config',required=False,
                    default='~/.aws/config',type=str,
                    help='supply config file name')
parser.add_argument('-s','--secrets',required=False,
                    default='~/.aws/credentials',type=str,
                    help='supply credentials file name')
parser.add_argument('-p','--profile',required=False,
                    default='default',type=str,
                    help='supply aws profile file name')

args=vars(parser.parse_args())

bucket=args['bucket']
object_key=args['object']
if args['method']=='get':
    http_method='GET'
else:
    http_method='PUT'
expiration=args['expiration']
config=args['config']
secrets=args['secrets']
profile=args['profile']

if config == default_config:
    config_env=os.environ.get('AWS_CONFIG_FILE')
    if config_env != None:
        config=config_env
        config_path=os.path.expanduser(config_env)
    else:
        config_path=os.path.expanduser(default_config)
else:
    config_path=os.path.expanduser(config)

if secrets == default_secrets:
    secrets_env=os.environ.get('AWS_SHARED_CREDENTIALS_FILE')
    if secrets_env != None:
        secrets=secrets_env
        secrets_path=os.path.expanduser(secrets_env)
    else:
        secrets_path=os.path.expanduser(default_secrets)
else:
    secrets_path=os.path.expanduser(secrets)

profile_env=os.environ.get('AWS_PROFILE')
access_key=os.environ.get('AWS_ACCESS_KEY_ID')
secret_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
endpoint=os.environ.get('AWS_ENDPOINT_URL')
region=os.environ.get('AWS_REGION')

if profile_env!=None: profile=profile_env
e,r=get_config(config_path,profile)
a,s=get_secrets(secrets_path,profile)

if region==None: region=r
if endpoint==None: endpoint=e
if access_key==None: access_key=a
if secret_key==None: secret_key=s

err=False
if region==None:
    print ("region is not provided",file=sys.stderr)
    err=True
if endpoint==None:
    print ("endpoint is not provided",file=sys.stderr)
    err=True
if access_key==None:
    print ("access_key is not provided",file=sys.stderr)
    err=True
if secret_key==None:
    print ("secret_key is not provided",file=sys.stderr)
    err=True

if err: sys.exit(1)

host=host_regexp.match(endpoint).groups()[0]

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
