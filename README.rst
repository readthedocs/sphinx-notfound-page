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


Customization
-------------

There are some configs that you can modify in your ``conf.py`` file,

notfound_template (str)
    Default: ``'page.html'``
notfound_context (dict)
    Default: ``{'body': '<h1>Page not found</h1>\n\nThanks for trying.'}``
notfound_pagename (str)
    Default: ``'404'``
notfound_default_language (str)
    Default: ``'en'``
notfound_default_version (str)
    Default: ``'latest'``
notfound_no_urls_prefix (bool)
    Default: ``False``

Thanks
------

**Strongly** based on @ericholscher's solution from https://github.com/rtfd/readthedocs.org/issues/353
