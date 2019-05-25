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


.. warning::

   If you open the ``404.html`` file on the browser,
   you will see that all of the images and css does not display properly.
   This is because all the URLs are absolute and since the file is being rendered from ``file://`` in the browser,
   it does not know where to find those resources.

   Do not worry too much about this, this is the expected behavior and those resources will appear once the docs are deployed.


.. note::

   This extension requires,

   * Python 2.7+ or 3.x
   * Sphinx 1.5+ or 2.x
