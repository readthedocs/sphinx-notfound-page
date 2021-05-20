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

    if sphinx.version_info >= (4, 0):
        return '<link rel="stylesheet" type="text/css" href="{href}" />'.format(href=href)
    else:
        return '<link rel="stylesheet" href="{href}" type="text/css" />'.format(href=href)


def _get_js_html_link_tag(language, version, filename):
    if not language and not version:
        src = '/_static/{filename}'.format(filename=filename)
    else:
        src = '/{language}/{version}/_static/{filename}'.format(
            language=language,
            version=version,
            filename=filename,
        )

    if sphinx.version_info < (2, 4, 0):
        return '<script type="text/javascript" src="{src}"></script>'.format(src=src)
    else:
        # #6925: html: Remove redundant type="text/javascript" from <script> elements
        return '<script src="{src}"></script>'.format(src=src)
