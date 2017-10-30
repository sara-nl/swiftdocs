.. _owncloud:

********
Owncloud
********

.. note:: **Note:** Since Nextcloud and Owncloud only support keystone V2 authentication, this will only work for users having a local keystone account.

In this page you will find a link to a video giving you information on how to do the coupling of SWIFT to an Owncloud or Nextcloud instance as external storage.

.. raw:: html

    <iframe width="1120" height="630" src="https://www.youtube.com/embed/RW9Fp_LfYIQ" frameborder="0" allowfullscreen></iframe>

If you use tools like **duck** or **rclone** to sync complete directories with the files in them, they will not be visible right away in Onwcloud or Nextcloud. For every directory a zero-byte object needs to be created with a name ending with a slash (/) and content type **httpd/unix-directory**. Then all directories and files will pop up in Owncloud and Nextcloud. You can do this using a command like:

.. code-block:: console

   curl -i -X PUT -d "" -H "X-Auth-Token: <token>" -H "Content-Type:httpd/unix-directory" <storage url>/<container>/<directory name ending with a slash (/) >

For example, with two levels of directories you would create objects like: **dir1/dir2/**.

