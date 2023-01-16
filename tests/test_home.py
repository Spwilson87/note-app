import pytest

from flask.testing import FlaskClient
from app import create_app

app = create_app()
@pytest.fixture
def client():
    return app.test_client()


def test_sign_up_status_code(client: FlaskClient):
    """should be a successful GET request"""
    response = client.get('/sign_up')
    statuscode = response.status_code
    assert (statuscode == 200)

def test_sign_up_content(client: FlaskClient):
    response = client.get("/sign_up")
    assert response.content_type, "html"

    # check returned data
def test_sign_up_data(client: FlaskClient):
    response = client.get("/sign_up")
    assert (b'Sign Up' in response.data)
    assert (b'Username' in response.data)
    assert (b'Password' in response.data)
    assert (b'Log In' in response.data)
    assert (b'Already have an account? Log In' in response.data)  


def test_sign_up_bad_http_method(client: FlaskClient):
    """should return a Method Not Allowed response"""
    resp = client.post('/sign_up')
    assert resp.status_code == 400
    