import requests
from .endpoints import *


def post_credentials(payload):
    headers = {
        'Content-type': 'application/json'
    }

    return requests.post(
        url=f'{restful_booker}/{Endpoint.auth}',
        json=payload,
        headers=headers
    )
