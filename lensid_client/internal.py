import json

import requests as r

from typing import Mapping, Optional, Tuple


RESOURCES = {
    'login': '/api/login/',
    'document': '/api/document/',
}

HEADERS = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}


def json_or_none(response:r.Response) -> Optional[Mapping[str, str]]:
    """
    Returns a valid JSON, when the response if not a valid JSON, returns `None`.
    """
    try:
        return response.json()
    except ValueError:
        return None


def login(post_func, domain:str, username:str, password:str) -> Tuple[Optional[str], r.Response]:
    """
    Returns a auth token and `requests.Response` as a tuple. When a request has not been successful, returns `None`
    as the token.
    - `domain` should not contain a trailing slash
    """

    def token_or_none(maybe_json:Mapping[str, str]) -> Optional[str]:
        return maybe_json.get('token', None) if maybe_json is not None else None

    response = post_func(domain + RESOURCES['login'], json={'username': username, 'password': password},
                         headers=HEADERS)
    return ((token_or_none(json_or_none(response)), response) if response.status_code == 200 else (None, response))


def scan_document(post_func, domain:str, token:str, document:Mapping[str, str]) -> Tuple[Optional[dict], r.Response]:
    """
    Returns a scanned document and `requests.Response` as a tuple. When a request has not been successful, return `None`
    as the document.
    - `domain` should not contain a trailing slash
    - `document` should be a dictionary
    """
    response = post_func(domain + RESOURCES['document'], json=document, headers={'Authorization': token, **HEADERS})
    return ((json_or_none(response), response) if response.status_code == 201 else (None, response))


def login_and_scan(post_func, domain:str, username:str, password:str, document:Mapping[str, str],
                   token:str=None) -> Tuple[Optional[dict], r.Response]:
    """
    Returns a scanned document and `requests.Response` as a tuple. When a request has not been successful, return `None`
    as the document. First it tries to use a given auth `token`. When the `token` is not valid, tries to log in via
    given `username` and `password`.
    - `domain` should not contain a trailing slash
    - `document` should be a dictionary
    """
    if not token:
        token, login_response = login(post_func, domain, username, password)

        if not token:
            return (None, login_response)

    document, document_response = scan_document(post_func, domain, token, document)
    if document_response.status_code == 401:
        token, login_response = login(post_func, domain, username, password)

    if not token:
        return (None, login_response)

    return scan_document(post_func, domain, token, document)
