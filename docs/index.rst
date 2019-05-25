Welcome to sphinx-notfound-page!
================================

``sphinx-notfound-page`` is a Sphinx_ extension to create custom 404 pages and help you to generate proper resource links (js, css, images, etc) to render the page properly.

This extension was originally developed to be used on `Read the Docs`_ but it can be used in other hosting services as well.


Why I need this extension?
--------------------------

Sphinx does not create a 404 page by default.
Although, you can create it by adding a simple ``404.rst`` file to your docs but...

If you are reading this documentation,
you may already experienced the problem that all your images do no load,
all your styles are broken and all the javascript events does not work,
when accessing the 404 page of your documentation.

So, if you want to have a nice custom 404 page,
you will probably want to use this extension to avoid this headache
and let the extension handle these URLs properly for you.



.. toctree::
   :maxdepth: 1
   :caption: Contents:

   installation
   configuration
   get-involved
   who-is-using-it
   faq


.. _Sphinx: https://www.sphinx-doc.org/
.. _Read the Docs: https://readthedocs.org
