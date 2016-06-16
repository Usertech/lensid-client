Lens ID client
==============

A client library for Lens ID API.

[![Build Status](https://travis-ci.org/Usertech/lensid-client.svg?branch=master)](https://travis-ci.org/Usertech/lensid-client)

Prerequisites
-------------

- Python 3.5 or newer


Examples
--------

```python
from lensid_client import login
from lensid_client.utils import build_snapshot

token, response = login('http://127.0.0.1', 'username@example.com', 'password')

data = {
    'document_type': 2,
    'front_side': build_snapshot('open-source-logo.png', '/path/to/open-source-logo.png', 'image/png'),
    'back_side': build_snapshot('open-source-logo.png', '/path/to/open-source-logo.png', 'image/png'),
}

document, response = scan_document('http://127.0.0.1', token, data)
```

For more details see tests or PyDocs.
