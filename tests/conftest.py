# pylint: disable=C0116
# pylint: disable=W0621
# pylint: disable=import-error
"""Test module for Blueprint Plaza routes."""
import pytest
from flask_caching import Cache
from ..app import app as flask_app



@pytest.fixture
def app():
    flask_app.config.update({
        'TESTING': True,
        'CACHE_TYPE': 'simple'
    })
    return flask_app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def cache(app):
    return Cache(app, config={'CACHE_TYPE': 'simple'})

@pytest.fixture
def runner(app):
    return app.test_cli_runner()
