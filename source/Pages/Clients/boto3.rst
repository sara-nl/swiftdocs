.. _boto3:

*****
Boto3
*****

In this page you will find documentation about the **boto3 S3** library by Amazon written in python you can use to access swift using the S3 API.

You can install the boto3 library by:

.. code-block:: bash

    pip install boto3

Information on the S3 part of this library is at: http://boto3.readthedocs.io/en/latest/reference/services/s3.html

Below you find a piece of example code to:

- list buckets
- create a bucket
- upload an object
- adapt object metadata
- get metadata
- list the objects in a bucket
- download an object
- delete an object
- delete a bucket


.. code-block:: python

    #!/usr/bin/env python
    import boto3
    import json,sys

    b3bucket='boto3bucket'
    b3object='boto3object'
    b3file='boto3file'

    resource = boto3.client('s3',
                            'NL',
                            endpoint_url='https://proxy.swift.surfsara.nl',
                            aws_access_key_id='ACCESS_KEY',
                            aws_secret_access_key='SECRET_KEY')
    print ('\n\n')




    print ('Print list of buckets')
    response=resource.list_buckets()
    rv=response['ResponseMetadata']['HTTPStatusCode']
    if rv<200 and rv>=300: sys.exit(1) # List buckets failed
    print json.dumps(response, indent=4,sort_keys=True, default=str)
    print ('\n\n')




    print ('Create bucket '+b3bucket)
    response=resource.create_bucket(Bucket=b3bucket)
    rv=response['ResponseMetadata']['HTTPStatusCode']
    if rv<200 and rv>=300: sys.exit(1) # Create bucket failed
    print ('\n\n')




    print ('Upload file '+b3file+' to bucket as object '+b3object)
    with open(b3file, 'rb') as data:
        resource.upload_fileobj(data, b3bucket, b3object)
    print ('\n\n')




    print ("Set metadata 'my-new-key=my-new-value' to object "+b3object)
    copy_source = {
        'Bucket': b3bucket,
        'Key': b3object
    }
    resource.copy(
        copy_source, b3bucket, b3object,
        ExtraArgs={
            "Metadata": {
                "my-new-key": "my-new-value"
            },
            "MetadataDirective": "REPLACE"
        }
    )
    print ('\n\n')
    


    print ('Get metadata of '+b3object)
    response=resource.head_object(Bucket=b3bucket, Key=b3object)
    rv=response['ResponseMetadata']['HTTPStatusCode']
    if rv<200 and rv>=300: sys.exit(1) # Get metadata failed
    print json.dumps(response['Metadata'], indent=4,sort_keys=True, default=str)
    print ('\n\n')



    print ('List objects in bucket '+b3bucket)
    response=resource.list_objects(Bucket=b3bucket)
    rv=response['ResponseMetadata']['HTTPStatusCode']
    if rv<200 and rv>=300: sys.exit(1) # List objects failed
    print json.dumps(response, indent=4,sort_keys=True, default=str)
    print ('\n\n')




    print ('Download object '+b3object+' as file '+b3file+'_downloaded')
    with open(b3file+'_downloaded', 'wb') as data:
        resource.download_fileobj(b3bucket, b3object, data)
    print ('\n\n')




    print ('Delete object '+b3object)
    response=resource.delete_object(Bucket=b3bucket,Key=b3object)
    rv=response['ResponseMetadata']['HTTPStatusCode']
    if rv<200 and rv>=300: sys.exit(1) # Delete object failed
    print ('\n\n')




    print ('Delete bucket '+b3bucket)
    response=resource.delete_bucket(Bucket=b3bucket)
    rv=response['ResponseMetadata']['HTTPStatusCode']
    if rv<200 and rv>=300: sys.exit(1) # Delete bucket failed
    print ('\n\n')
