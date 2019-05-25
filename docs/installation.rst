Installation
============

Install the package

.. tabs::

   .. tab:: from PyPI

      .. prompt:: bash

         pip install sphinx-notfound-page

   .. tab:: from GitHub

      .. prompt:: bash

         pip install git+https://github.com/rtfd/sphinx-notfound-page@master


Once we have the package installed,
we have to configure it on our Sphinx documentation.
To do this, add this extension to your Sphinx's extensions in the ``conf.py`` file.

.. code-block:: python

   # conf.py
   extensions = [
        # ... other extensions here
        'notfound.extension',
   ]


After installing the package and adding the extension in the ``conf.py`` file,
you can build your documentation again and you will see a new file called ``404.html`` in your documentation's build output.


.. note::

   This extension requires,

   * Python 2.7.x or 3.x
   * Sphinx 1.x or 2.x
