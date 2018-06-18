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

When a file is requested that does not exist, then a 404 error code is returned. The command above will make sure that a file 404error.html is returned when it is present. You can do this for all HTTP return codes.

Enable a custom listings style sheet

.. code-block:: console

      swift post -m 'web-listings-css:style.css' mywebpage

.. code-block:: html

    <html>
    <h1>
    See the web page <a href="mywebsite/page.html">here</a>.
    </h1>
    </html>

.. image:: /Images/web1.png
