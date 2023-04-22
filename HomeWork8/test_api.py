import requests
import pytest

BASE_URL = 'https://restful-booker.herokuapp.com'
endpoint_booking = '/booking'
endpoint_auth = '/auth'
STATUS_OK = 200
STATUS_OK_DELETE = 201
STATUS_NOT_FOUND = 404


@pytest.fixture(scope='module')
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f'{BASE_URL}{endpoint_auth}', json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token


@pytest.fixture(scope='module')
def id_booking():
    payload = {
        "firstname": "Jany",
        "lastname": "Brown",
        "totalprice": 110,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-02",
            "checkout": "2019-01-02"
        },
        "additionalneeds": "Dinner"
    }
    response = requests.post(f'{BASE_URL}{endpoint_booking}', json=payload)
    assert response.status_code == STATUS_OK
    id_booking = response.json()['bookingid']
    yield id_booking


def test_user_autorization():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f'{BASE_URL}{endpoint_auth}', json=payload)
    assert response.status_code == STATUS_OK
    response_data = response.json()
    assert 'token' in response_data
    print(f'\n{response_data}')


def test_get_all_booking():
    response = requests.get(f'{BASE_URL}{endpoint_booking}')
    assert response.status_code == STATUS_OK
    print(f'\n{len(response.json())}')
    header = ('Connection', 'keep-alive')
    assert header in response.headers.items()
    key = 'Connection'
    assert key in response.headers.keys()


def test_get_booking_with_id():
    response = requests.get(f'{BASE_URL}{endpoint_booking}/1')
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    for key in expected_keys:
        assert key in response_data.keys()
    print(f'\n{response_data}')


def test_create_booking():
    payload = {
        "firstname": "Jany",
        "lastname": "Brown",
        "totalprice": 110,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-02",
            "checkout": "2019-01-02"
        },
        "additionalneeds": "Supper"
    }
    response = requests.post(f'{BASE_URL}{endpoint_booking}', json=payload)
    response_data = response.json()
    assert response.status_code == STATUS_OK
    # id_booking = response.json()['bookingid']
    print(f'\n{response_data}')


def test_get_my_booking(id_booking):
    response = requests.get(f'{BASE_URL}{endpoint_booking}/{id_booking}')
    assert response.status_code == STATUS_OK
    assert response.json()['firstname'] == 'Jany'
    print(f'\n{response.json()}')


def test_update_booking(auth_token, id_booking):
    payload = {
        "firstname": "Jany",
        "lastname": "Brown",
        "totalprice": 125,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-02",
            "checkout": "2019-01-02"
        },
        "additionalneeds": "Lunch"
    }
    header = {'Cookie': f'token={auth_token}'}
    response = requests.put(f'{BASE_URL}{endpoint_booking}/{id_booking}', json=payload, headers=header)
    assert response.status_code == STATUS_OK

    response_get = requests.get(f'{BASE_URL}{endpoint_booking}/{id_booking}')
    response_data = response_get.json()
    assert response_get.status_code == STATUS_OK
    assert response_data['totalprice'] == payload['totalprice']
    assert response_data['additionalneeds'] == payload['additionalneeds']
    print(f'\n{response_data}')


def test_partial_update_booking(auth_token, id_booking):
    payload = {
        "lastname": "Gold",
        "totalprice": 150
    }
    header = {'Cookie': f'token={auth_token}'}
    response = requests.patch(f'{BASE_URL}{endpoint_booking}/{id_booking}', json=payload, headers=header)
    assert response.status_code == STATUS_OK

    response_get = requests.get(f'{BASE_URL}{endpoint_booking}/{id_booking}')
    response_data = response_get.json()
    assert response_get.status_code == STATUS_OK
    assert response_data['lastname'] == payload['lastname']
    assert response_data['totalprice'] == payload['totalprice']
    print(f'\n{response_data}')


def test_delete_booking(auth_token, id_booking):
    header = {'Cookie': f'token={auth_token}'}
    response = requests.delete(f'{BASE_URL}{endpoint_booking}/{id_booking}', headers=header)
    assert response.status_code == STATUS_OK_DELETE
    response_get = requests.get(f'{BASE_URL}{endpoint_booking}/{id_booking}')
    assert response_get.status_code == STATUS_NOT_FOUND
