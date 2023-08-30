class ConnectedState:
    def __init__(self, connection):
        self.connection = connection

    def get_name(self):
        return 'connected'

    def connect(self):
        raise Exception('Connection has established already')

    def disconnect(self):
        self.connection.set_state('disconnected')

    def write(self, data):
        self.connection.buffer.append(data)
