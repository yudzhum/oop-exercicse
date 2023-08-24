class User:
    def __init__(self, name):
        self.name = name
        self.type = 'user'

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


class Guest:
    def __init__(self):
        self.name = 'Guest'
        self.type = 'guest'

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


MAPPING = {
    'guest': lambda guest: f'Nice to meet you {guest.get_name()}!',
    'user': lambda user: f'Hello {user.get_name()}!',
}


def greet(user):
    return MAPPING[user.get_type()](user)
