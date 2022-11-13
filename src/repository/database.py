class DatabaseConnetor(object):
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connect()

    def connect(self):
        raise NotImplementedError