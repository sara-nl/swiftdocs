.. _staticweb:

************************
Serving Static Web Pages
************************

SWIFT offers the possibility to serve data in containers as a static web site. This can be done by following the steps below.

First create a container

.. code-block:: console

      swift post mywebpage

Make sure that everythting is world readable

.. code-block:: console

      swift post -r '.r:*,.rlistings' mywebpage

You should be able to hit paths that have an index.html without needing to type the index.html part. So you need to set an index file directive

.. code-block:: console

      swift post -m 'web-index:index.html' mywebpage


Allow listing if no index.html file exists

.. code-block:: console

      swift post -m 'web-listings: true' mywebpage

Set custom error pages

.. code-block:: console

      swift post -m 'web-error:error.html' mywebpage

When a file is requested that does not exist, then a **404** error code is returned. The command above will make sure that a file **404error.html** is returned when it is present. You can do this for all HTTP return codes.

Enable a custom listings style sheet

.. code-block:: console

      swift post -m 'web-listings-css:style.css' mywebpage


=======
Example
=======

Suppose we have the following html files **index.html** which links to **mywebpage/page.html** both shown below. The page **mywebpage/page.html** displays the image **mywebsite/surfsaragreendisklogo.png**.

.. code-block:: html

    <!-- index.html -->
    <html>
    <h1>
    See the web page <a href="mywebsite/page.html">here</a>.
    </h1>
    </html>

.. code-block:: html

    <!-- page.html -->
    <html>
    <img src="surfsaragreendisklogo.png">
    </html>

This web site is uploaded as follows:

.. image:: /Images/upload.png

Now we can view the website on: **<STORAGE_URL>/mywebpage/**.

.. image:: /Images/web1.png

When you click on the link you get:

.. image:: /Images/web2.png

Suppose we create a custom **404error.html** file which looks as follows:

.. code-block:: html

    <html>
    <h1>
    This page is nowhere to be found
    </h1>
    </html>

We upload this file:

.. code-block:: console

      swift upload mywebpage 404error.html

Then we get the following if we request a file that does not exist.

.. image:: /Images/foetsie.png

