class AuthorisePayload:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def build(self):
        return f"""{{
            "username": "{self.username}",
            "password": "{self.password}"
        }}"""
