import json
from pprint import pprint

def _register(client, username, password):
    return client.post(
        '/users/',
        data=json.dumps({'username': username,'password': password}),
        content_type='application/json'
    ).json

def _login(client, username, password):
    return client.post(
        '/login/',
        data=json.dumps({'username': username,'password': password}),
        content_type='application/json'
    ).json


def _access(client, access_token):
    return client.get(
        '/secret/',
        headers={"Authorization": f"Bearer {access_token}"},
        content_type='application/json'
    ).json

def test_no_access(client):
    resp = client.get('/secret/', content_type='application/json')
    assert not resp.json['success']

def test_register(client):
    new_user_data = _register(client, 'test', '1234')
    assert new_user_data['success']
    assert new_user_data['data']['access_token']
    assert new_user_data['data']['refresh_token']
    assert new_user_data['data']['id']

def test_wrong_password(client):
    login = _login(client, 'test', '2345')
    assert not login['success']

def test_login(client):
    login = _login(client, 'test', '1234')
    assert login['success']
    assert login['success']
    assert login['data']['access_token']
    assert login['data']['refresh_token']
    assert login['data']['id']

def test_access(client):
    login = _login(client, 'test', '1234')
    access = _access(client, login['data']['access_token'])
    assert access['success']
    assert access['data']['answer'] == 42