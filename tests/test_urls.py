import os
import pytest
import sphinx
import shutil
import subprocess

from utils import _get_css_html_link_tag, _get_js_html_link_tag

srcdir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'examples',
    'default',
)

rstsrcdir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'examples',
    '404rst',
)

extensiondir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'examples',
    'extension',
)

@pytest.fixture(autouse=True, scope='function')
def remove_sphinx_build_output():
    """Remove _build/ folder, if exist."""
    for path in (srcdir, rstsrcdir, extensiondir):
        build_path = os.path.join(path, '_build')
        if os.path.exists(build_path):
            shutil.rmtree(build_path)


@pytest.mark.sphinx(srcdir=srcdir)
def test_parallel_build():
    # TODO: migrate to `app.build(..., parallel=2)` after merging
    # https://github.com/sphinx-doc/sphinx/pull/8257
    subprocess.check_call('sphinx-build -j 2 -W -b html tests/examples/parallel-build build', shell=True)

@pytest.mark.sphinx(srcdir=srcdir)
def test_404_page_created(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

@pytest.mark.sphinx('epub', srcdir=srcdir)
def test_404_page_not_created(app, status, warning):
    assert app.builder.embedded
    app.build()
    path = app.outdir / '404.html'
    assert not path.exists()

@pytest.mark.sphinx(
    srcdir=srcdir,
    # Sphinx changed the default theme to basic in version 8.1.0
    # (https://github.com/sphinx-doc/sphinx/pull/12776), but our
    # tests depend heavily on the specifics of alabaster.
    confoverrides={'html_theme': 'alabaster'},
)
def test_default_settings(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()
    content = path.read_text()

    if sphinx.version_info < (6, 0):
        cssclass = "shortcut "
    else:
        cssclass = ""

    if sphinx.version_info < (7, 4):
        alt = "Logo"
    else:
        alt = "Logo of Python"

    chunks = [
        '<h1>Page not found</h1>',
        "Unfortunately we couldn't find the content you were looking for.",
        '<title>Page not found &#8212; Python  documentation</title>',

        # favicon and logo
        f'<link rel="{cssclass}icon" href="/en/latest/_static/favicon.png"/>',
        f'<img class="logo" src="/en/latest/_static/logo.svg" alt="{alt}"/>',

        # sidebar URLs
        '<h1 class="logo"><a href="/en/latest/index.html">Python</a></h1>',
        '<form class="search" action="/en/latest/search.html" method="get">',
        '<li><a href="/en/latest/index.html">Documentation overview</a><ul>',

        # resources
        _get_css_html_link_tag(app, 'en', 'latest', 'alabaster.css'),
        _get_css_html_link_tag(app, 'en', 'latest', 'pygments.css'),
        '<link rel="stylesheet" href="/en/latest/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content

@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_context': {'title': 'My custom title', 'body': '<h1>Boo!</h1>My bad.'},
    },
)
def test_context_settings(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()
    content = path.read_text()

    chunks = [
        '<h1>Boo!</h1>',
        'My bad.',
        '<title>My custom title &#8212; Python  documentation</title>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_pagename': '500',
    },
)
def test_pagename_setting(app, status, warning):
    app.build()
    path = app.outdir / '500.html'
    assert path.exists()


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_urls_prefix': '/language/version/',
        'html_theme': 'alabaster',
    },
)
def test_urls_prefix_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    if sphinx.version_info < (6, 0):
        cssclass = "shortcut "
    else:
        cssclass = ""

    if sphinx.version_info < (7, 4):
        alt = "Logo"
    else:
        alt = "Logo of Python"

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/language/version/index.html">Python</a></h1>',
        '<form class="search" action="/language/version/search.html" method="get">',
        '<li><a href="/language/version/index.html">Documentation overview</a><ul>',

        # favicon and logo
        f'<link rel="{cssclass}icon" href="/language/version/_static/favicon.png"/>',
        f'<img class="logo" src="/language/version/_static/logo.svg" alt="{alt}"/>',

        # resources
        _get_css_html_link_tag(app, 'language', 'version', 'alabaster.css'),
        _get_css_html_link_tag(app, 'language', 'version', 'pygments.css'),
        '<link rel="stylesheet" href="/language/version/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_urls_prefix': None,
        'html_theme': 'alabaster',
    },
)
def test_urls_prefix_setting_none(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    if sphinx.version_info < (6, 0):
        cssclass = "shortcut "
    else:
        cssclass = ""

    if sphinx.version_info < (7, 4):
        alt = "Logo"
    else:
        alt = "Logo of Python"


    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/index.html">Python</a></h1>',
        '<form class="search" action="/search.html" method="get">',
        '<li><a href="/index.html">Documentation overview</a><ul>',

        # favicon and logo
        f'<link rel="{cssclass}icon" href="/_static/favicon.png"/>',
        f'<img class="logo" src="/_static/logo.svg" alt="{alt}"/>',

        # resources
        _get_css_html_link_tag(app, '', '', 'alabaster.css'),
        _get_css_html_link_tag(app, '', '', 'pygments.css'),
        '<link rel="stylesheet" href="/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content

    assert "The config value `notfound_urls_prefix' has type `NoneType', defaults to `str'" not in warning.getvalue()
    assert "build succeeded." in status.getvalue()

@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_template': 'template.html',
        'notfound_context': {
            'body': 'The body goes here',
            'title': 'Custom title',
            'special_setting': 'a special value',
        },
    },
)
def test_template_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        'Custom title',
        'The body goes here',
        '<p>This is rendered using a custom template</p>',
        '<p>... which has a custom context as well: a special value</p>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=rstsrcdir,
    confoverrides={
        'version': '2.5.1',
        'html_theme': 'alabaster',
    },
)
def test_custom_404_rst_source(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        # custom 404.rst file content
        '<title>Oh, oh - Page not found &#8212; Python  documentation</title>',
        '<p>This is a custom 404.rst file.</p>',
        '<p>This file should be rendered instead of the default one.</p>',
        "<p>Variables Sphinx substitution should be allowed here.\nExample, version: 2.5.1.</p>",

        # sidebar URLs
        '<h1 class="logo"><a href="/en/latest/index.html">Python</a></h1>',
        '<form class="search" action="/en/latest/search.html" method="get">',
        '<li><a href="/en/latest/index.html">Documentation overview</a><ul>',

        # resources
        _get_css_html_link_tag(app, 'en', 'latest', 'alabaster.css'),
        _get_css_html_link_tag(app, 'en', 'latest', 'pygments.css'),
        '<link rel="stylesheet" href="/en/latest/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=rstsrcdir)
def test_image_on_404_rst_source(app, status, warning):
    app.build()

    # Check the image was added to the builder/environment images
    assert 'test.png' in app.builder.images
    assert 'test.png' in app.env.images

    # Check the image was copied into the output dir
    path = app.outdir / '_images' / 'test.png'
    assert path.exists()

    path = app.outdir / '_images' / 'loudly-crying-face.png'
    assert path.exists()

    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        # .. image::
        '<img alt="An image" src="/en/latest/_images/test.png" />',
        '<img alt="Image from folder" src="/en/latest/_images/loudly-crying-face.png" />',

    ]

    if sphinx.version_info < (7, 2):
        chunks.extend([
            # .. figure::
            '<figure class="align-default" id="id1">\n<img alt="/en/latest/_images/test.png" src="/en/latest/_images/test.png" />\n<figcaption>\n<p><span class="caption-text">Description.</span><a class="headerlink" href="#id1" title="Permalink to this image">¶</a></p>\n</figcaption>\n</figure>',
        ])
    else:
        chunks.extend([
            # .. figure::
            '<figure class="align-default" id="id1">\n<img alt="/en/latest/_images/test.png" src="/en/latest/_images/test.png" />\n<figcaption>\n<p><span class="caption-text">Description.</span><a class="headerlink" href="#id1" title="Link to this image">¶</a></p>\n</figcaption>\n</figure>',
        ])


    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=rstsrcdir)
def test_image_looks_like_absolute_url(app, status, warning):
    app.build()

    path = app.outdir / '_images' / 'https.png'
    assert path.exists()

    path = app.outdir / '404.html'
    assert path.exists()
    content = path.read_text()

    chunks = [
        '<img alt="PATH looking as an URL" src="/en/latest/_images/https.png" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=rstsrcdir)
def test_image_absolute_url(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()
    content = path.read_text()

    chunks = [
        '<img alt="Read the Docs Logo" src="https://read-the-docs-guidelines.readthedocs-hosted.com/_images/logo-dark.png" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    buildername='dirhtml',
    confoverrides={'html_theme': 'alabaster'},
)
def test_urls_for_dirhtml_builder(app, status, warning):
    app.build()
    path = app.outdir / '404' / 'index.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/en/latest/search/" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/en/latest/chapter/">Chapter</a></li>',

        # resources
        _get_css_html_link_tag(app, 'en', 'latest', 'alabaster.css'),
        _get_css_html_link_tag(app, 'en', 'latest', 'pygments.css'),
        '<link rel="stylesheet" href="/en/latest/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=srcdir)
def test_sphinx_resource_urls(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        # Sphinx's resources URLs
        _get_js_html_link_tag(app, 'en', 'latest', 'doctools.js'),
    ]

    if sphinx.version_info < (6, 0):
        chunks.extend([
            _get_js_html_link_tag(app, 'en', 'latest', 'underscore.js'),
            _get_js_html_link_tag(app, 'en', 'latest', 'jquery.js'),
        ])

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_urls_prefix': '/ja/default/',
        'html_theme': 'alabaster',
    },
)
def test_toctree_urls_notfound_default(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/ja/default/search.html" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/ja/default/chapter.html">Chapter</a></li>',

        # resources
        _get_css_html_link_tag(app, 'ja', 'default', 'alabaster.css'),
        _get_css_html_link_tag(app, 'ja', 'default', 'pygments.css'),
        '<link rel="stylesheet" href="/ja/default/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={'html_theme': 'alabaster'},
)
def test_toctree_links(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        '<h3>Navigation</h3>',
        '<li class="toctree-l1"><a class="reference internal" href="/en/latest/chapter-i.html">Chapter I</a></li>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_urls_prefix': '/pt-br/stable/',
        'html_theme': 'alabaster',
    },
)
def test_toctree_links_custom_settings(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        '<h3>Navigation</h3>',
        '<li class="toctree-l1"><a class="reference internal" href="/pt-br/stable/chapter-i.html">Chapter I</a></li>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=rstsrcdir,
)
def test_automatic_orphan(app, status, warning):
    app.build()
    assert app.env.metadata['404'] == {'orphan': True, 'nosearch': True}


@pytest.mark.sphinx(srcdir=extensiondir)
def test_resources_from_extension(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()
    chunks = [
        '<link rel="stylesheet" type="text/css" href="/en/latest/_static/css_added_by_extension.css" />',
        '<link rel="stylesheet" type="text/css" href="/en/latest/_static/css_added_by_extension.css" />',
        _get_js_html_link_tag(app, 'en', 'latest', 'js_added_by_extension.js'),
    ]

    for chunk in chunks:
        assert chunk in content

@pytest.mark.environ(
    READTHEDOCS='True',
)
@pytest.mark.sphinx(srcdir=rstsrcdir)
def test_special_readthedocs_urls(environ, app, status, warning):
    app.add_js_file('/_/static/javascript/readthedocs-doc-embed.js')

    app.build()

    path = app.outdir / '404.html'
    assert path.exists()

    content = path.read_text()

    chunks = [
        # Link included manually
        '<a class="reference external" href="/_/static/javascript/readthedocs-doc-embed.js">readthedocs-doc-embed.js</a>',
    ]

    # Javascript library loaded via Sphinx
    chunks.append('<script src="/_/static/javascript/readthedocs-doc-embed.js"></script>')

    for chunk in chunks:
        assert chunk in content
