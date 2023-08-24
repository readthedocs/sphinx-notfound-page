import sphinx


def _get_css_html_link_tag(language, version, filename):
    if not language and not version:
        href = '/_static/{filename}'.format(filename=filename)
    else:
        href = '/{language}/{version}/_static/{filename}'.format(
            language=language,
            version=version,
            filename=filename,
        )

    if sphinx.version_info >= (7, 2):
        # it requires `?v={hash}`
        hashes = {
            "pygments.css": "4f649999",
            "alabaster.css": "039e1c02",
        }
        filehash = hashes.get(filename)
        if filehash:
            href = f"{href}?v={filehash}"

    return '<link rel="stylesheet" type="text/css" href="{href}" />'.format(href=href)


def _get_js_html_link_tag(language, version, filename):
    if not language and not version:
        src = '/_static/{filename}'.format(filename=filename)
    else:
        src = '/{language}/{version}/_static/{filename}'.format(
            language=language,
            version=version,
            filename=filename,
        )

    if sphinx.version_info >= (7, 2):
        # it requires `?v={hash}`
        hashes = {
            "documentation_options.js": "5929fcd5",
            "doctools.js": "888ff710",
            "sphinx_highlight.js": "dc90522c",
        }
        filehash = hashes.get(filename)
        if filehash:
            src = f"{src}?v={filehash}"

    # #6925: html: Remove redundant type="text/javascript" from <script> elements
    return '<script src="{src}"></script>'.format(src=src)

