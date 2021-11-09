# -*- coding: utf-8 -*-

import os
import docutils
import pytest
import sphinx
import shutil
import subprocess
import warnings

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
    for path in (srcdir, rstsrcdir):
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


@pytest.mark.sphinx(srcdir=srcdir)
def test_default_settings(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()
    content = open(path).read()

    chunks = [
        '<h1>Page not found</h1>',
        "Unfortunately we couldn't find the content you were looking for.",
        '<title>Page not found &#8212; Python  documentation</title>',

        # favicon and logo
        '<link rel="shortcut icon" href="/en/latest/_static/favicon.png"/>',
        '<img class="logo" src="/en/latest/_static/logo.svg" alt="Logo"/>',

        # sidebar URLs
        '<h1 class="logo"><a href="/en/latest/index.html">Python</a></h1>',
        '<form class="search" action="/en/latest/search.html" method="get">',
        '<li><a href="/en/latest/index.html">Documentation overview</a><ul>',

        # resources
        _get_css_html_link_tag('en', 'latest', 'alabaster.css'),
        _get_css_html_link_tag('en', 'latest', 'pygments.css'),
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
    content = open(path).read()

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
        'notfound_default_language': 'ja',
    },
)
def test_default_language_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/ja/latest/index.html">Python</a></h1>',
        '<form class="search" action="/ja/latest/search.html" method="get">',
        '<li><a href="/ja/latest/index.html">Documentation overview</a><ul>',

        # favicon and logo
        '<link rel="shortcut icon" href="/ja/latest/_static/favicon.png"/>',
        '<img class="logo" src="/ja/latest/_static/logo.svg" alt="Logo"/>',

        # resources
        _get_css_html_link_tag('ja', 'latest', 'alabaster.css'),
        _get_css_html_link_tag('ja', 'latest', 'pygments.css'),
        '<link rel="stylesheet" href="/ja/latest/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_version': 'customversion',
    },
)
def test_default_version_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/en/customversion/index.html">Python</a></h1>',
        '<form class="search" action="/en/customversion/search.html" method="get">',
        '<li><a href="/en/customversion/index.html">Documentation overview</a><ul>',

        # favicon and logo
        '<link rel="shortcut icon" href="/en/customversion/_static/favicon.png"/>',
        '<img class="logo" src="/en/customversion/_static/logo.svg" alt="Logo"/>',

        # resources
        _get_css_html_link_tag('en', 'customversion', 'alabaster.css'),
        _get_css_html_link_tag('en', 'customversion', 'pygments.css'),
        '<link rel="stylesheet" href="/en/customversion/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_no_urls_prefix': True,
    },
)
def test_no_urls_prefix_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/index.html">Python</a></h1>',
        '<form class="search" action="/search.html" method="get">',
        '<li><a href="/index.html">Documentation overview</a><ul>',

        # resources
        _get_css_html_link_tag('', '', 'alabaster.css'),
        _get_css_html_link_tag('', '', 'pygments.css'),
        '<link rel="stylesheet" href="/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_urls_prefix': '/language/version/',
    },
)
def test_urls_prefix_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/language/version/index.html">Python</a></h1>',
        '<form class="search" action="/language/version/search.html" method="get">',
        '<li><a href="/language/version/index.html">Documentation overview</a><ul>',

        # favicon and logo
        '<link rel="shortcut icon" href="/language/version/_static/favicon.png"/>',
        '<img class="logo" src="/language/version/_static/logo.svg" alt="Logo"/>',

        # resources
        _get_css_html_link_tag('language', 'version', 'alabaster.css'),
        _get_css_html_link_tag('language', 'version', 'pygments.css'),
        '<link rel="stylesheet" href="/language/version/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_urls_prefix': None,
    },
)
def test_urls_prefix_setting_none(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/index.html">Python</a></h1>',
        '<form class="search" action="/search.html" method="get">',
        '<li><a href="/index.html">Documentation overview</a><ul>',

        # favicon and logo
        '<link rel="shortcut icon" href="/_static/favicon.png"/>',
        '<img class="logo" src="/_static/logo.svg" alt="Logo"/>',

        # resources
        _get_css_html_link_tag('', '', 'alabaster.css'),
        _get_css_html_link_tag('', '', 'pygments.css'),
        '<link rel="stylesheet" href="/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_language': 'es',
        'notfound_default_version': 'customversion',
        'notfound_no_urls_prefix': True,
    },
)
def test_no_urls_prefix_setting_preference(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/index.html">Python</a></h1>',
        '<form class="search" action="/search.html" method="get">',
        '<li><a href="/index.html">Documentation overview</a><ul>',

        # resources
        _get_css_html_link_tag('', '', 'alabaster.css'),
        _get_css_html_link_tag('', '', 'pygments.css'),
        '<link rel="stylesheet" href="/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_version': 'v2.0.5',
        'notfound_default_language': 'pt',
    },
)
def test_default_version_language_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/pt/v2.0.5/index.html">Python</a></h1>',
        '<form class="search" action="/pt/v2.0.5/search.html" method="get">',
        '<li><a href="/pt/v2.0.5/index.html">Documentation overview</a><ul>',

        # resource URLs
        _get_css_html_link_tag('pt', 'v2.0.5', 'alabaster.css'),
        _get_css_html_link_tag('pt', 'v2.0.5', 'pygments.css'),
        '<link rel="stylesheet" href="/pt/v2.0.5/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


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

    content = open(path).read()

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
    },
)
def test_custom_404_rst_source(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

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
        _get_css_html_link_tag('en', 'latest', 'alabaster.css'),
        _get_css_html_link_tag('en', 'latest', 'pygments.css'),
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

    content = open(path).read()

    chunks = [
        # .. image::
        '<img alt="An image" src="/en/latest/_images/test.png" />',
        '<img alt="Image from folder" src="/en/latest/_images/loudly-crying-face.png" />',
    ]

    # .. figure::
    if sphinx.version_info < (2, 0):
        chunks.append(
            '<div class="figure" id="id1">\n<img alt="/en/latest/_images/test.png" src="/en/latest/_images/test.png" />\n<p class="caption"><span class="caption-text">Description.</span></p>\n</div>'
        )
    elif sphinx.version_info < (2, 1):
        chunks.append(
            u'<div class="figure align-center" id="id1">\n<img alt="/en/latest/_images/test.png" src="/en/latest/_images/test.png" />\n<p class="caption"><span class="caption-text">Description.</span><a class="headerlink" href="#id1" title="Permalink to this image">¶</a></p>\n</div>',
        )
    elif docutils.__version_info__ < (0, 17, 0):
        chunks.append(
            u'<div class="figure align-default" id="id1">\n<img alt="/en/latest/_images/test.png" src="/en/latest/_images/test.png" />\n<p class="caption"><span class="caption-text">Description.</span><a class="headerlink" href="#id1" title="Permalink to this image">¶</a></p>\n</div>',
        )
    else:
        chunks.append(
            u'<figure class="align-default" id="id1">\n<img alt="/en/latest/_images/test.png" src="/en/latest/_images/test.png" />\n<figcaption>\n<p><span class="caption-text">Description.</span><a class="headerlink" href="#id1" title="Permalink to this image">¶</a></p>\n</figcaption>\n</figure>',
        )

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=rstsrcdir)
def test_image_looks_like_absolute_url(app, status, warning):
    app.build()

    path = app.outdir / '_images' / 'https.png'
    assert path.exists()

    path = app.outdir / '404.html'
    assert path.exists()
    content = open(path).read()

    chunks = [
        '<img alt="PATH looking as an URL" src="/en/latest/_images/https.png" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=rstsrcdir)
def test_image_absolute_url(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists() == True
    content = open(path).read()

    chunks = [
        '<img alt="Read the Docs Logo" src="https://read-the-docs-guidelines.readthedocs-hosted.com/_images/logo-dark.png" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    buildername='dirhtml',
)
def test_urls_for_dirhtml_builder(app, status, warning):
    app.build()
    path = app.outdir / '404' / 'index.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/en/latest/search/" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/en/latest/chapter/">Chapter</a></li>',

        # resources
        _get_css_html_link_tag('en', 'latest', 'alabaster.css'),
        _get_css_html_link_tag('en', 'latest', 'pygments.css'),
        '<link rel="stylesheet" href="/en/latest/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    buildername='dirhtml',
    confoverrides={
        'notfound_no_urls_prefix': True,
    },
)
def test_no_prefix_urls_for_dirhtml_builder(app, status, warning):
    app.build()
    path = app.outdir / '404' / 'index.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/search/" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/chapter/">Chapter</a></li>',

        # resources
        _get_css_html_link_tag('', '', 'alabaster.css'),
        _get_css_html_link_tag('', '', 'pygments.css'),
        '<link rel="stylesheet" href="/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=srcdir)
def test_sphinx_resource_urls(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # Sphinx's resources URLs
        _get_js_html_link_tag('en', 'latest', 'jquery.js'),
        _get_js_html_link_tag('en', 'latest', 'underscore.js'),
        _get_js_html_link_tag('en', 'latest', 'doctools.js'),
    ]

    # This file was added to all the HTML pages in Sphinx>=1.8. However, it was
    # only required for search page. Sphinx>=3.4 fixes this and only adds it on
    # search. See (https://github.com/sphinx-doc/sphinx/blob/v3.4.0/CHANGES#L87)
    if (1, 8) <= sphinx.version_info < (3, 4, 0):
        chunks.append(
            _get_js_html_link_tag('en', 'latest', 'language_data.js'),
        )

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_version': 'default',
        'notfound_default_language': 'ja',
    },
)
def test_toctree_urls_notfound_default(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/ja/default/search.html" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/ja/default/chapter.html">Chapter</a></li>',

        # resources
        _get_css_html_link_tag('ja', 'default', 'alabaster.css'),
        _get_css_html_link_tag('ja', 'default', 'pygments.css'),
        '<link rel="stylesheet" href="/ja/default/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
)
def test_toctree_links(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        '<h3>Navigation</h3>',
        '<li class="toctree-l1"><a class="reference internal" href="/en/latest/chapter-i.html">Chapter I</a></li>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_language': 'pt-br',
        'notfound_default_version': 'stable',
    },
)
def test_toctree_links_custom_settings(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        '<h3>Navigation</h3>',
        '<li class="toctree-l1"><a class="reference internal" href="/pt-br/stable/chapter-i.html">Chapter I</a></li>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.environ(
    READTHEDOCS_VERSION='v2.0.5',
)
@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_language': 'pt-br',
    },
)
def test_toctree_links_language_setting_version_environment(environ, app, status, warning):
    app.build()

    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        '<h3>Navigation</h3>',
        '<li class="toctree-l1"><a class="reference internal" href="/pt-br/v2.0.5/chapter-i.html">Chapter I</a></li>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.environ(
    READTHEDOCS_LANGUAGE='fr',
)
@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_version': 'master',
    },
)
def test_toctree_links_version_setting_language_environment(environ, app, status, warning):
    app.build()

    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        '<h3>Navigation</h3>',
        '<li class="toctree-l1"><a class="reference internal" href="/fr/master/chapter-i.html">Chapter I</a></li>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.environ(
    READTHEDOCS_VERSION='stable',
    READTHEDOCS_LANGUAGE='ja',
)
@pytest.mark.sphinx(srcdir=srcdir)
def test_toctree_links_version_language_environment(environ, app, status, warning):
    app.build()

    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()

    chunks = [
        '<h3>Navigation</h3>',
        '<li class="toctree-l1"><a class="reference internal" href="/ja/stable/chapter-i.html">Chapter I</a></li>',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=rstsrcdir,
)
def test_automatic_orphan(app, status, warning):
    app.build()
    if sphinx.version_info >= (3, 0, 0):
        assert app.env.metadata['404'] == {'orphan': True, 'nosearch': True}
    else:
        assert app.env.metadata['404'] == {'orphan': True}


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_language': 'ja',
        'notfound_default_version': 'stable',
        'notfound_no_urls_prefix': True,
    },
)
@pytest.mark.xfail(reason='Not sure how to capture warnings from events')
def test_deprecation_warnings(app, status, warning):
    messages = [
        'notfound_default_language is deprecated. Use "notfound_urls_prefix" instead.',
        'notfound_default_version is deprecated. Use "notfound_urls_prefix" instead.',
        'notfound_no_urls_prefix is deprecated. Use "notfound_urls_prefix" instead.',
    ]

    with warnings.catch_warnings(record=True) as warn:
        warnings.simplefilter('always')
        app.build()

        assert len(warn) == 3
        assert issubclass(warn[-1].category, DeprecationWarning)
        for w in warn:
            assert w.message in messages

    path = app.outdir / '404.html'
    assert path.exists()


@pytest.mark.sphinx(srcdir=extensiondir)
def test_resources_from_extension(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists()

    content = open(path).read()
    chunks = [
        '<link rel="stylesheet" type="text/css" href="/en/latest/_static/css_added_by_extension.css" />',
        '<link rel="stylesheet" type="text/css" href="/en/latest/_static/css_added_by_extension.css" />',
        _get_js_html_link_tag('en', 'latest', 'js_added_by_extension.js'),
    ]

    for chunk in chunks:
        assert chunk in content
