|Build| |PyPI| |License| |Issues|

Welcome to sphinx-notfound-page!
================================

``sphinx-notfound-page`` is a Sphinx_ extension to create custom 404 pages and generate proper resource links (js, css, images, etc) to render the page properly.

This extension was originally developed to be used on `Read the Docs`_, but it can be used in other documentation hosting services as well.

Source code repository (and issue tracker):
    https://github.com/rtfd/sphinx-notfound-page/

Why do I need this extension?
-----------------------------

Sphinx does not create a 404 page by default. You can create one by adding a
``404.rst`` file to your docs, but on the resulting ``404.html`` page the
links  to images, stylesheets, and javascript resources will be broken.

Use the ``sphinx-notfound-page`` extension to handle these URLs properly for
you, creating a custom 404 page that works seamlessly and easily.


.. toctree::
   :maxdepth: 1
   :caption: Contents

   installation
   configuration
   how-it-works
   get-involved
   who-is-using-it
   faq


.. toctree::
   :maxdepth: 1
   :caption: API Reference

   autoapi/notfound/index


.. _Sphinx: https://www.sphinx-doc.org/
.. _Read the Docs: https://readthedocs.org

.. |Build| image:: https://travis-ci.org/rtfd/sphinx-notfound-page.svg?branch=master
   :target: https://travis-ci.org/rtfd/sphinx-notfound-page
   :alt: Build status
.. |PyPI| image:: https://img.shields.io/pypi/v/sphinx-notfound-page.svg
   :target: https://pypi.org/project/sphinx-notfound-page
   :alt: Current PyPI version
.. |License| image:: https://img.shields.io/github/license/rtfd/sphinx-notfound-page.svg
   :target: LICENSE
   :alt: Repository license
.. |Issues| image:: https://img.shields.io/github/issues/rtfd/sphinx-notfound-page.svg
   :target: https://github.com/rtfd/sphinx-notfound-page/issues
   :alt: Open issues
