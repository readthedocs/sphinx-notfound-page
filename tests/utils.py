import sphinx


def _get_css_html_link_tag(app, language, version, filename):
    if not language and not version:
        href = '/_static/{filename}'.format(filename=filename)
    else:
        href = '/{language}/{version}/_static/{filename}'.format(
            language=language,
            version=version,
            filename=filename,
        )

    if sphinx.version_info >= (7, 1):
        # it requires `?v={hash}`
        if sphinx.version_info < (7, 2):
            from sphinx.builders.html import _file_checksum
        else:
            from sphinx.builders.html._assets import _file_checksum
        filehash = _file_checksum(app.outdir / "_static", filename)
        if filehash:
            href = f"{href}?v={filehash}"

    return '<link rel="stylesheet" type="text/css" href="{href}" />'.format(href=href)


def _get_js_html_link_tag(app, language, version, filename):
    if not language and not version:
        src = '/_static/{filename}'.format(filename=filename)
    else:
        src = '/{language}/{version}/_static/{filename}'.format(
            language=language,
            version=version,
            filename=filename,
        )

    if sphinx.version_info >= (7, 1):
        # it requires `?v={hash}`
        if sphinx.version_info < (7, 2):
            from sphinx.builders.html import _file_checksum
        else:
            from sphinx.builders.html._assets import _file_checksum
        filehash = _file_checksum(app.outdir / "_static", filename)
        if filehash:
            src = f"{src}?v={filehash}"

    # #6925: html: Remove redundant type="text/javascript" from <script> elements
    return '<script src="{src}"></script>'.format(src=src)

