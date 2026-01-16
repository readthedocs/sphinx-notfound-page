import sphinx


def _get_css_html_link_tag(app, language, version, filename):
    if not language and not version:
        href = f'/_static/{filename}'
    else:
        href = f'/{language}/{version}/_static/{filename}'

    if sphinx.version_info >= (7, 1):
        # it requires `?v={hash}`
        if sphinx.version_info < (7, 2):
            from sphinx.builders.html import _file_checksum
        else:
            from sphinx.builders.html._assets import _file_checksum
        filehash = _file_checksum(app.outdir / "_static", filename)
        if filehash:
            href = f"{href}?v={filehash}"

    return f'<link rel="stylesheet" type="text/css" href="{href}" />'


def _get_js_html_link_tag(app, language, version, filename):
    if not language and not version:
        src = f'/_static/{filename}'
    else:
        src = f'/{language}/{version}/_static/{filename}'

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
    return f'<script src="{src}"></script>'

