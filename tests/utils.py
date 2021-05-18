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
