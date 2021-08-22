.. _manysmallfilesupload:

**************************
Uploading many small files
**************************

When you want to upload a folder containing many small files, then :ref:`rclone <rclone>` and :ref:`s5cmd <s5cmd>` are suitable tools.

rclone
-----

Rclone uses by default 4 parallel transfers when copying a whole directory with files. 
For large files this may be fine but if the directory contains many small files (<10MB) it may be worthwhile to use a large number of concurrent transfers. For example, something like this:

.. code-block:: console

    rclone copy --transfers=100 -P /path/to/folder/with/small/files S3:mybucket

In this case we have used 100 concurrent transfers but you may play around with this value to see what works best for you. Here we have defined the remote **S3** as in :ref:`rclone <rclone>`. 

s5cmd
-----

.. code-block:: console

    s5cmd --numworkers 256 --endpoint-url https://proxy.swift.surfsara.nl cp --destination-region NL /path/to/folder/with/small/files s3://mybucket

Here **numworkers** which is the number of parallel transfers, is by default 256. This is already quite suitable for the many small files use case.
But also here, you may play around a bit with this value to see what's best.
