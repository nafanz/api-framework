from enum import StrEnum

restful_booker = 'https://restful-booker.herokuapp.com'


class Endpoint(StrEnum):
    auth = 'auth'
    booking = 'booking'
