import requests

url_booking = 'https://restful-booker.herokuapp.com/booking'


def all_bookings():
    return requests.get(url=url_booking)


def specific_booking(identifier, accept):
    headers = {
        'Accept': accept
    }

    return requests.get(
        url=f'{url_booking}/{identifier}',
        headers=headers
    )


def create_booking(payload, content_type):
    headers = {
        'Accept': 'application/json',
        'Content-type': content_type
    }

    return requests.post(
        url_booking,
        payload,
        headers=headers
    )


def delete_booking(identifier, token):
    headers = {
        'Cookie': f'token={token}'
    }

    return requests.delete(
        url=f'{url_booking}/{identifier}',
        headers=headers
    )

