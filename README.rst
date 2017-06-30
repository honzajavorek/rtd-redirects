rtd-redirects
=============

|PyPI version| |Build Status|

Manage redirects in the `ReadTheDocs <http://readthedocs.org/>`__ admin, programmatically.

Installation
------------

Requires **Python 3.6** and higher.

.. code:: sh

    $ pip install rtd-redirects

Usage
-----

.. code:: sh

    $ rtd-redirects project-name ./redirects.yml --username=honzajavorek

Uploads redirects defined in the ``redirects.yml`` file to ReadTheDocs redirects administration of the ``project-name`` project.

The tool uses ReadTheDocs' HTML interface (there's no official API for redirects), so you need to provide your username and password. HTTPS is used to transfer the credentials to ReadTheDocs.

``rtd-redirects`` tries to be idempotent, i.e. you can run it several times in row and it should always end with the same results. If there are any redirects with the same source path, the tool will replace them with whatever is defined in the ``redirects.yml`` file. Existing redirects which do not collide with contents of ``redirects.yml`` won't be affected.

redirects.yml
-------------

Only **page redirects** are supported at the moment. The format of the file is as follows:

.. code:: yaml

    redirects:
      # Following redirects have to be done because we've migrated from MkDocs to Sphinx
      "/example/": "/example.html"
      "/python/": "/python.html"

      # Following pages has been removed in favor of sections
      "/green.html": "/colors.html#green"

      # Following redirects are only for convenience
      "/praha.html": "/prague.html"

Why `YAML <https://en.wikipedia.org/wiki/YAML>`__? Because it's easy to read by humans, easy to write by humans, and above all, it has support for comments. Redirects are *corrections* and you should document why they're necessary.

License: MIT
------------

© 2017-? Honza Javorek mail@honzajavorek.cz

This work is licensed under `MIT
license <https://en.wikipedia.org/wiki/MIT_License>`__.

.. |PyPI version| image:: https://badge.fury.io/py/rtd-redirects.svg
   :target: https://badge.fury.io/py/rtd-redirects
.. |Build Status| image:: https://travis-ci.org/honzajavorek/rtd-redirects.svg?branch=master
   :target: https://travis-ci.org/honzajavorek/rtd-redirects
