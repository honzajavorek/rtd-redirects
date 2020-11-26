rtd-redirects
=============

Manage redirects in the `ReadTheDocs <http://readthedocs.org/>`__ admin, programmatically. Addressing the `rtfd/readthedocs.org#2904 <https://github.com/rtfd/readthedocs.org/issues/2904>`__ issue.

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
      # we've migrated from MkDocs to Sphinx
      "/example/": "/example.html"
      "/python/": "/python.html"

      # page removed in favor of section
      "/green.html": "/colors.html#green"

      # only for convenience
      "/praha.html": "/prague.html"

Why `YAML <https://en.wikipedia.org/wiki/YAML>`__? Because it's easy to read by humans, easy to write by humans, and above all, it has support for comments. Redirects are *corrections* and you should document why they're necessary.


Usage with ReadTheDocs PRO
--------------------------

If you are using a commercial edition of the RTD (from ``readthedocs.com`` instead of ``readthedocs.org``), please specify ``--pro`` flag in the command, like this

.. code:: sh

    $ rtd-redirects project-name ./redirects.yml --username=honzajavorek --pro

There is also an opposite flag ``--free`` which is added by default, so can be omitted


License: MIT
------------

© 2017-? Honza Javorek mail@honzajavorek.cz

This work is licensed under `MIT
license <https://en.wikipedia.org/wiki/MIT_License>`__.
