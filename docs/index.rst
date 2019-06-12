Welcome to sphinx-notfound-page!
================================

``sphinx-notfound-page`` is a Sphinx_ extension to create custom 404 pages and help you to generate proper resource links (js, css, images, etc) to render the page properly.

This extension was originally developed to be used on `Read the Docs`_ but it can be used in other hosting services as well.

Online documentation:
    https://sphinx-notfound-page.readthedocs.io/

Source code repository (and issue tracker):
    https://github.com/rtfd/sphinx-notfound-page/

Badges:
    |Build| |PyPI version| |Docs badge| |License|


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
.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-notfound-page.svg
   :target: https://pypi.org/project/sphinx-notfound-page
   :alt: Current PyPI version
.. |Docs badge| image:: https://readthedocs.org/projects/sphinx-notfound-page/badge/?version=latest
   :target: https://sphinx-notfound-page.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation status
.. |License| image:: https://img.shields.io/github/license/rtfd/sphinx-notfound-page.svg
   :target: LICENSE
   :alt: Repository license
