import pytest
from app import app as _app
from app.models.auth import User


@pytest.fixture(scope='session')
def app():
    with _app.app_context():
        yield _app
        User.delete_all()


@pytest.fixture(scope='function')
def client(app):
    with _app.test_client() as client:
        yield client
