# -*- coding: utf-8 -*-

import os
import pytest
import sphinx


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


# NOTE: ``SphinxTestApp`` unfortunately does not accept ``outdir`` to use a
# different one per test run
@pytest.mark.sphinx(srcdir=srcdir)
def test_404_page_created(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists() == True


@pytest.mark.sphinx(srcdir=srcdir)
def test_default_settings(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists() == True
    content = open(path).read()

    chunks = [
        '<h1>Page not found</h1>',
        'Thanks for trying.',
        '<title>Page not found &#8212; Python  documentation</title>',

        # sidebar URLs
        '<h1 class="logo"><a href="/en/latest/index.html">Python</a></h1>',
        '<form class="search" action="/en/latest/search.html" method="get">',
        '<li><a href="/en/latest/index.html">Documentation overview</a><ul>',

        # resources
        '<link rel="stylesheet" href="/en/latest/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/en/latest/_static/pygments.css" type="text/css" />',
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
    assert path.exists() == True
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
    assert path.exists() == True


@pytest.mark.sphinx(
    srcdir=srcdir,
    confoverrides={
        'notfound_default_language': 'ja',
    },
)
def test_default_language_setting(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/ja/latest/index.html">Python</a></h1>',
        '<form class="search" action="/ja/latest/search.html" method="get">',
        '<li><a href="/ja/latest/index.html">Documentation overview</a><ul>',

        # resources
        '<link rel="stylesheet" href="/ja/latest/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/ja/latest/_static/pygments.css" type="text/css" />',
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
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/en/customversion/index.html">Python</a></h1>',
        '<form class="search" action="/en/customversion/search.html" method="get">',
        '<li><a href="/en/customversion/index.html">Documentation overview</a><ul>',

        # resources
        '<link rel="stylesheet" href="/en/customversion/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/en/customversion/_static/pygments.css" type="text/css" />',
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
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/index.html">Python</a></h1>',
        '<form class="search" action="/search.html" method="get">',
        '<li><a href="/index.html">Documentation overview</a><ul>',

        # resources
        '<link rel="stylesheet" href="/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/_static/pygments.css" type="text/css" />',
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
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/index.html">Python</a></h1>',
        '<form class="search" action="/search.html" method="get">',
        '<li><a href="/index.html">Documentation overview</a><ul>',

        # resources
        '<link rel="stylesheet" href="/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/_static/pygments.css" type="text/css" />',
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
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<h1 class="logo"><a href="/pt/v2.0.5/index.html">Python</a></h1>',
        '<form class="search" action="/pt/v2.0.5/search.html" method="get">',
        '<li><a href="/pt/v2.0.5/index.html">Documentation overview</a><ul>',

        # resource URLs
        '<link rel="stylesheet" href="/pt/v2.0.5/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/pt/v2.0.5/_static/pygments.css" type="text/css" />',
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
    assert path.exists() == True

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
    assert path.exists() == True

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
        '<link rel="stylesheet" href="/en/latest/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/en/latest/_static/pygments.css" type="text/css" />',
        '<link rel="stylesheet" href="/en/latest/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=rstsrcdir)
def test_image_on_404_rst_source(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # .. image::
        '<img alt="An image" src="/en/latest/test.png" />',
    ]

    # .. figure::
    if sphinx.version_info < (2, 0):
        chunks.append(
            '<div class="figure" id="id1">\n<img alt="/en/latest/test.png" src="/en/latest/test.png" />\n<p class="caption"><span class="caption-text">Description.</span></p>\n</div>'
        )
    else:
        chunks.append(
            u'<div class="figure align-center" id="id1">\n<img alt="/en/latest/test.png" src="/en/latest/test.png" />\n<p class="caption"><span class="caption-text">Description.</span><a class="headerlink" href="#id1" title="Permalink to this image">¶</a></p>\n</div>',
        )

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(
    srcdir=srcdir,
    buildername='dirhtml',
)
def test_urls_for_dirhtml_builder(app, status, warning):
    app.build()
    path = app.outdir / '404' / 'index.html'
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/en/latest/search/" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/en/latest/chapter/">Chapter</a></li>',

        # resources
        '<link rel="stylesheet" href="/en/latest/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/en/latest/_static/pygments.css" type="text/css" />',
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
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/search/" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/chapter/">Chapter</a></li>',

        # resources
        '<link rel="stylesheet" href="/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/_static/pygments.css" type="text/css" />',
        '<link rel="stylesheet" href="/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content


@pytest.mark.sphinx(srcdir=srcdir)
def test_sphinx_resource_urls(app, status, warning):
    app.build()
    path = app.outdir / '404.html'
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # Sphinx's resources URLs
        '<script type="text/javascript" src="/en/latest/_static/jquery.js"></script>',
        '<script type="text/javascript" src="/en/latest/_static/underscore.js"></script>',
        '<script type="text/javascript" src="/en/latest/_static/doctools.js"></script>',
    ]

    if sphinx.version_info >= (1, 8):
        chunks.append(
            '<script type="text/javascript" src="/en/latest/_static/language_data.js"></script>',
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
    assert path.exists() == True

    content = open(path).read()

    chunks = [
        # sidebar URLs
        '<form class="search" action="/ja/default/search.html" method="get">',
        '<li class="toctree-l1"><a class="reference internal" href="/ja/default/chapter.html">Chapter</a></li>',

        # resources
        '<link rel="stylesheet" href="/ja/default/_static/alabaster.css" type="text/css" />',
        '<link rel="stylesheet" href="/ja/default/_static/pygments.css" type="text/css" />',
        '<link rel="stylesheet" href="/ja/default/_static/custom.css" type="text/css" />',
    ]

    for chunk in chunks:
        assert chunk in content
