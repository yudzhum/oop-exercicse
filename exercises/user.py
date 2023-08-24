
class User():
    def __init__(self, email, current_subscription=None):
        self.email = email
        self.current_subscription = current_subscription 

    def get_current_subscription(self):
        return self.current_subscription

    def is_admin(self):
        return self.email == 'ya@hexlet.io'
