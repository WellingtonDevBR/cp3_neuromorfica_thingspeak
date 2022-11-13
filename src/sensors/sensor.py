
class Sensor:
    def __init__(self, response=None):
        self.fields = []
        self.response = response

    def set_column_names(self):
        raise NotImplementedError 
    
    def get_data_from_channel(self):
        raise NotImplementedError

    def get_column_names(self):
        raise NotImplementedError

    def get_columns_data(self):
        raise NotImplementedError

    def list_to_database_columns(self):
        raise NotImplementedError

    def get_last_entry_id(self):
        raise NotImplementedError
