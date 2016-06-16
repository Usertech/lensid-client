import base64

from typing import Mapping


def get_file_as_base64(file_path:str) -> str:
    """
    Returns a file content as base64.
    """
    with open(file_path, 'rb') as output:
        return str(base64.b64encode(output.read()))


def build_snapshot(file_name:str, file_path:str, content_type:str) -> Mapping[str, str]:
    """
    Converts given parameters into a snapshot dict for a request.
    """
    return {
        'filename': file_name,
        'content_type': content_type,
        'content': get_file_as_base64(file_path),
    }
