class DisconnectedState:
    def __init__(self, connection):
        self.connection = connection

    def get_name(self):
        return 'disconnected'

    def connect(self):
        self.connection.set_state('connected')

    def disconnect(self):
        raise Exception('Connection already disconnected')

    def write(self):
        raise Exception('It is not possible write to closed connection')