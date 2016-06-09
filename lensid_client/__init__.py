import requests as r

from typing import Mapping, Optional, Tuple

import lensid_client.internal as internal


def login(domain:str, username:str, password:str) -> Tuple[Optional[str], r.Response]:
    """
    Returns a auth token and `requests.Response` as a tuple. When a request has not been successful, returns `None`
    as the token.
    - `domain` should not contain a trailing slash
    """
    return internal.login(r.post, domain, username, password)


def scan_document(domain:str, token:str, document:Mapping[str, str]) -> Tuple[Optional[dict], r.Response]:
    """
    Returns a scanned document and `requests.Response` as a tuple. When a request has not been successful, return `None`
    as the document.
    - `domain` should not contain a trailing slash
    - `document` should be a dictionary
    """
    return internal.scan_document(r.post, domain, token, document)


def login_and_scan(domain:str, username:str, password:str, document:Mapping[str, str],
                   token:str=None) -> Tuple[Optional[dict], r.Response]:
    """
    Returns a scanned document and `requests.Response` as a tuple. When a request has not been successful, return `None`
    as the document. First it tries to use a given auth `token`. When the `token` is not valid, tries to log in via
    given `username` and `password`.
    - `domain` should not contain a trailing slash
    - `document` should be a dictionary
    """
    return internal.login_and_scan(r.post, domain, username, password, document, token)
