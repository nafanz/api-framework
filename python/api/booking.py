import requests
from .endpoints import *


def all_bookings():
    return requests.get(
        url=restful_booker
    )


def specific_booking(identifier, accept):
    headers = {
        'Accept': accept
    }

    return requests.get(
        url=f'{restful_booker}/{Endpoint.booking}/{identifier}',
        headers=headers
    )


def create_booking(payload, content_type):
    headers = {
        'Accept': 'application/json',
        'Content-type': content_type
    }

    return requests.post(
        url=f'{restful_booker}/{Endpoint.booking}',
        json=payload,
        headers=headers
    )


def delete_booking(identifier, token):
    headers = {
        'Cookie': f'token={token}'
    }

    return requests.delete(
        url=f'{restful_booker}/{Endpoint.booking}/{identifier}',
        headers=headers
    )

