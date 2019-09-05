import pytest


@pytest.fixture(scope='function')
def environ(request, monkeypatch):
    """
    Fixture to define environment variables before Sphinx App is created.

    The test case needs to be marked as
    ``@pytest.mark.environ(VARIABLE='value')`` with all the environment
    variables wanted to define. Also, the test has to use this fixture before
    the ``app`` once to have effect.

    This idea is borrowed from,
        https://github.com/sphinx-doc/sphinx/blob/3f6565df6323534e69d797003d8cb20e99c2c255/sphinx/testing/fixtures.py#L30
    """
    if hasattr(request.node, 'iter_markers'):  # pytest-3.6.0 or newer
        markers = request.node.iter_markers('environ')
    else:
        markers = request.node.get_marker('environ')
    pargs = {}
    kwargs = {}

    if markers is not None:
        # to avoid stacking positional args
        for info in reversed(list(markers)):
            for i, a in enumerate(info.args):
                pargs[i] = a
            kwargs.update(info.kwargs)

    for name, value in kwargs.items():
        monkeypatch.setenv(name, value)
