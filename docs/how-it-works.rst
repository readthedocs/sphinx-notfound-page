How It Works
============

The extension subscribes to some events emitted by Sphinx application.
When these events are triggered,
our functions are called and they manipulate the doctree and context passed to the template.


Events subscribed
-----------------

There are 3 main events that this extension subscribes,

* ``doctree-resolved``
* ``html-collect-pages``
* ``html-page-context``

Each one has an specific goal persuading the same objective:
make all the resources URLs absolutes.


doctree-resolved
~~~~~~~~~~~~~~~~

Once Sphinx has parsed our source files, this event is triggered.
Here, we check if the page being rendered is ``notfound_pagename`` and in that case,
we replace all the URLs for ``.. image::``, ``.. figure::`` and other directives to point the right path.


html-collect-pages
~~~~~~~~~~~~~~~~~~

After all HTML pages are collected and this event is emitted,
we check for the existence of a ``404`` page already.
If the is one, we do nothing here.
On the other hand, if the user has not defined this page,
we render the template ``notfound_template`` with the context ``notfound_context``.


html-page-context
~~~~~~~~~~~~~~~~~

Immediately before the template is rendered with the context, this event is emitted.
At this point, we override ``pathto`` [#pathto]_ function with our custom one that will generate the proper URLs.
We also override ``toctree`` [#toctree]_ key with the same content of the regular toctree but with all the URLs fixed to find the resources from the 404 page.

.. [#pathto] https://www.sphinx-doc.org/page/templating.html#pathto
.. [#toctree] https://www.sphinx-doc.org/page/templating.html#toctree
