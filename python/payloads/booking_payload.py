class BookingPayload:
    def __init__(self, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
        self.firstname = firstname
        self.lastname = lastname
        self.totalprice = totalprice
        self.depositpaid = depositpaid
        self.checkin = checkin
        self.checkout = checkout
        self.additionalneeds = additionalneeds

    def build(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": {
                "checkin": self.checkin,
                "checkout": self.checkout
            },
            "additionalneeds": self.additionalneeds
        }
