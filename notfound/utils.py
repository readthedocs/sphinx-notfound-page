from sphinx.builders.html import DirectoryHTMLBuilder


def replace_uris(app, doctree, nodetype, nodeattr):
    """
    Replace ``nodetype`` URIs from ``doctree`` to the proper one.

    :param app: Sphinx Application
    :type app: sphinx.application.Sphinx
    :param doctree: doctree representing the document
    :type doctree: docutils.nodes.document
    :param nodetype: type of node to replace URIs
    :type nodetype: docutils.nodes.Node
    :param nodeattr: node attribute to be replaced
    :type nodeattr: str
    """
    # https://github.com/sphinx-doc/sphinx/blob/2adeb68af1763be46359d5e808dae59d708661b1/sphinx/environment/adapters/toctree.py#L260-L266
    for node in doctree.traverse(nodetype):
        uri = node.attributes.get(nodeattr)  # somepage.html (or ../sompage.html)

        if isinstance(app.builder, DirectoryHTMLBuilder):
            # When the builder is ``DirectoryHTMLBuilder``, refuri will be
            # ``../somepage.html``. In that case, we want to remove the
            # initial ``../`` to make valid links
            if uri.startswith('../'):
                uri = uri.replace('../', '')

        if app.config.notfound_no_urls_prefix:
            uri = '/{filename}'.format(
                filename=uri,
            )
        else:
            uri = '/{language}/{version}/{filename}'.format(
                language=app.config.notfound_default_language,
                version=app.config.notfound_default_version,
                filename=uri,
            )
        node.replace_attr(nodeattr, uri)
