|Build| |PyPI version| |Docs badge| |License|

sphinx-notfound-page
====================

Create a custom 404 page with absolute URLs hardcoded.


Installation
------------

::

   pip install sphinx-notfound-page


Configuration
-------------

Add this extension in your ``conf.py`` file as:

.. code-block:: python

   extensions = [
    # ... other extensions here

    'notfound.extension',
   ]


Documentation
-------------

Check out the full documentation at https://sphinx-notfound-page.readthedocs.io/


Thanks
------

**Strongly** based on @ericholscher's solution from https://github.com/readthedocs/readthedocs.org/issues/353

.. |Build| image:: https://travis-ci.org/readthedocs/sphinx-notfound-page.svg?branch=master
   :target: https://travis-ci.org/readthedocs/sphinx-notfound-page
   :alt: Build status
.. |PyPI version| image:: https://img.shields.io/pypi/v/sphinx-notfound-page.svg
   :target: https://pypi.org/project/sphinx-notfound-page
   :alt: Current PyPI version
.. |Docs badge| image:: https://readthedocs.org/projects/sphinx-notfound-page/badge/?version=latest
   :target: https://sphinx-notfound-page.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation status
.. |License| image:: https://img.shields.io/github/license/readthedocs/sphinx-notfound-page.svg
   :target: LICENSE
   :alt: Repository license
