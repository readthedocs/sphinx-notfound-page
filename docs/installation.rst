Installation
============

1. Install the package:

.. tabs::

   .. tab:: from PyPI

      .. prompt:: bash

         pip install sphinx-notfound-page

   .. tab:: from GitHub

      .. prompt:: bash

         pip install git+https://github.com/readthedocs/sphinx-notfound-page@master


2. After installing the package,
configure it by adding the following extension to the ``conf.py`` file:

.. code-block:: python

   # conf.py
   extensions = [
        # ... other extensions here
        'notfound.extension',
   ]


3. Build your documentation again.
.. result:: A new ``404.html``file is created in the build output of your documentation.

.. note:important::

   If you open the ``404.html`` file in a browser, the images and css do not display properly.
   The URLs are absolute and the resources cannot be found at ``file://``.

   It is an expected behavior and those resources appear once the docs are deployed.


.. info::

   This extension requires:

   * Python 2.7+ or 3.x
   * Sphinx 1.5+ or 2.x
