class DatabaseConnetor(object):
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.connect()
        
    def connect(self):
        raise NotImplementedError
    
    def disconnect(self):
        raise NotImplementedError

    def create_database(self, database_name):
        raise NotImplementedError
    
    def create_table(self, table_name, columns):
        raise NotImplementedError
    
    def set_database(self, database_name):
        raise NotImplementedError
    
    def insert_data(self, columns, values):
        raise NotImplementedError
    
    def get_last_row(self, table_name):
        raise NotImplementedError
    
    