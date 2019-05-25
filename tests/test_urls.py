import os
import pytest


srcdir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'examples',
    'default',
)


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
        'Thanks for trying',
        '<title> &#8212; Python  documentation</title>',

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
