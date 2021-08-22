.. _largefilesupload:

*********************
Uploading large files
*********************

When you want to upload a small number of large files (>1GB) then :ref:`s5cmd <s5cmd>` would be a good choice. This tools uses parallelism in its uploads. 
Not only in terms of many concurrent uploads of a large number of files but 
it parallelises the upload of a single large file as well resulting in a very good performance. This can be done using the **-c** or **``--concurrency``** flag. This works as follows:

.. code-block:: console

    s5cmd --endpoint-url https://proxy.swift.surfsara.nl cp -c 64 --destination-region NL ./my_very_big_file s3://<mybucket>/<mybigfile>

In the example above the large file is concurrently uploaded in 64 chunks. But you may play around with this value to see what gives you the best performance.
