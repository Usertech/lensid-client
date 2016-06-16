import os

import requests
import responses

from lensid_client import login, scan_document
from lensid_client.internal import HEADERS, RESOURCES
from lensid_client.utils import build_snapshot


expected_token = 'asdf'
domain = 'http://127.0.0.1'


def test_login():
    username = 'obelix@rychmat.eu'
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST,
                 domain + RESOURCES['login'],
                 json={'token': expected_token,
                       'user': {'email': username,
                                'id': 1}},
                 status=200,
                 content_type=HEADERS['Content-Type'])
        token, response = login(domain, username, 'obelix')
        assert token == expected_token


def test_login_with_invalid_JSON():
    username = 'obelix@rychmat.eu'
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST,
                 domain + RESOURCES['login'],
                 body='an invalid JSON',
                 status=200,
                 content_type=HEADERS['Content-Type'])
        token, response = login(domain, username, 'obelix')
        assert None == token


success_response = {
    "fields": [
        {
            "id": 217,
            "final_value": None,
            "slug": "holders_signature",
            "additional_data": {}
        },
        {
            "id": 216,
            "final_value": "M",
            "slug": "sex",
            "additional_data": {}
        },
        {
            "id": 215,
            "final_value": "IDCZENOVAK<<<<JAN<<<<<<<<<<<<<<<<<<<11111111CZE8903222M18050635514<<<5",
            "slug": "mrz",
            "additional_data": {}
        },
        {
            "id": 214,
            "final_value": "1111111",
            "slug": "document_no",
            "additional_data": {}
        },
        {
            "id": 213,
            "final_value": "10.10.2020",
            "slug": "expiration_date",
            "additional_data": {}
        },
        {
            "id": 212,
            "final_value": "Česká Republika",
            "slug": "nationality",
            "additional_data": {}
        },
        {
            "id": 211,
            "final_value": "801010/1010",
            "slug": "personal_no",
            "additional_data": {}
        },
        {
            "id": 210,
            "final_value": "10.10.1980",
            "slug": "birth_date",
            "additional_data": {}
        },
        {
            "id": 209,
            "final_value": "Jan",
            "slug": "first_name",
            "additional_data": {}
        },
        {
            "id": 208,
            "final_value": "Novák",
            "slug": "last_name",
            "additional_data": {}
        },
        {
            "id": 207,
            "final_value": None,
            "slug": "photo",
            "additional_data": {}
        },
        {
            "id": 206,
            "final_value": "MěÚ PODBOŘANY",
            "slug": "authority",
            "additional_data": {}
        },
        {
            "id": 205,
            "final_value": "10.10.2010",
            "slug": "issue_date",
            "additional_data": {}
        },
        {
            "id": 204,
            "final_value": "svobodný",
            "slug": "marital_status",
            "additional_data": {}
        },
        {
            "id": 203,
            "final_value": "Novák",
            "slug": "maiden_name",
            "additional_data": {}
        },
        {
            "id": 202,
            "final_value": "KRYRY KOSTELNÍ 100 okr. LOUNY",
            "slug": "permanent_residence",
            "additional_data": {
                "municipality": "Kryry",
                "municipality_part": "Kryry",
                "street": "Kostelní",
                "city_district": None,
                "district": "Louny",
                "region": "Severočeský",
                "superior_region": "Ústecký kraj",
                "state": "Česká republika",
                "zip_code": 43981,
                "house_number": 24,
                "orientation_number": None,
                "orientation_char": None
            }
        },
        {
            "id": 201,
            "final_value": "PRAHA 4 PRAHA",
            "slug": "birthplace",
            "additional_data": {}
        }],
    "created_at": "2015-04-30T12:04:36.678Z",
    "document_type": {
        "id": 1,
        "_obj_name": "id_card_international_id1_2012"
    },
    "created_by": {
        "_rest_links": {
            "api-user": {
                "url": "/api/user",
                "methods": ["POST", "GET"]
            },
            "api-resource-user": {
                "url": "/api/user/2",
                "methods": ["PUT", "GET"]
            }
        },
        "id": 2,
        "_obj_name": "Gaul Obelix"
    },
    "id": 4
}


def get_snapshot(snapshot):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'media', snapshot)


def test_should_scan_document():
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST,
                 domain + RESOURCES['document'],
                 json=success_response,
                 status=201,
                 content_type=HEADERS['Content-Type'])
        data = {
            'document_type': 2,
            'front_side': build_snapshot('open-source-logo.png', get_snapshot('open-source-logo.png'), 'image/png'),
            'back_side': build_snapshot('open-source-logo.png', get_snapshot('open-source-logo.png'), 'image/png'),
        }
        document, response = scan_document(domain, expected_token, data)
        assert set(document.keys()) == {'document_type', 'fields', 'created_by', 'created_at', 'id'}
