.. _python-swift-client-osx:

***********************************************************
Installation Instructions of the Python SWIFT Client on OSX
***********************************************************

If you use Apple OS X, you may run into "System Integrity Protection" making installation hard. The easiest way, is to install the swift client into your home dir with ``--user`` and if needed ``--ignore-installed``, and make sure python uses that instead of the system version.

First, install your personal version of setuptools:

.. code-block:: console

    pip install --ignore-installed --user setuptools

Add these lines to your ``.profile``:

.. code-block:: console

    export PATH=~/Library/Python/2.7/bin:$PATH
    export MANPATH=~/Library/Python/2.7/share/man:$MANPATH

Reload your profile:

.. code-block:: console

    source .profile

Then create a file ``~/Library/Python/2.7/lib/python/site-packages/fix_mac_path.pth`` with this line:

.. code-block:: console

    import sys; std_paths=[p for p in sys.path if p.startswith('/System/') and not '/Extras/' in p]; sys.path=[p for p in sys.path if not p.startswith('/System/')]+std_paths

Then install the swift client:

.. code-block:: console

    pip install --user python-swiftclient

If you want to change your password, install also the openstack client

.. code-block:: console

    pip install --user --ignore-installed python-openstackclient

For more info, check the excellent answer by Matthias Fripp on https://apple.stackexchange.com/questions/209572/how-to-use-pip-after-the-os-x-el-capitan-upgrade.
