from sensors.sensor import Sensor

class SensorImplementation(Sensor):
    def __init__(self, response=None):
        super().__init__(response)
        self.set_column_names()

    def set_column_names(self):
        self.fields.append(self.response.get(
            'channel').get('field1') if True else None)
        self.fields.append(self.response.get(
            'channel').get('field2') if True else None)
        self.fields.append(self.response.get(
            'channel').get('field3') if True else None)
        self.fields.append(self.response.get(
            'channel').get('field4') if True else None)
        self.fields.append(self.response.get(
            'channel').get('field5') if True else None)
        self.fields.append(self.response.get(
            'channel').get('field6') if True else None)
        self.fields.append(self.response.get(
            'channel').get('field7') if True else None)
        self.fields.append(self.response.get(
            'channel').get('field8') if True else None)
        self.last_entry_id = self.response.get('channel').get('last_entry_id')

    def get_data_from_channel(self):
        return self.response.get('feeds')

    def get_column_names(self):
        new_list = []
        for value in self.fields:
            if value is not None:
                value = value.replace(' ', '_')
                value = value.replace('°', '')
                value = value.replace('[', '')
                value = value.replace(']', '')
                value = value.replace('.', '')
                value = value.replace('µ', '')
                value = value.replace('%', '')
                value = value.replace('(', '')
                value = value.replace(')', '')
                value = value.replace('=', '')
                value = value.replace("'\'", '')
                value = value.replace("/", '')
                value = value.replace('"', '')
                value = value.replace('0', '')
                value = value.replace('___', '_')
                value = value.replace('^', '')
                if value not in str(new_list):
                    new_list.append(value + ' VARCHAR(255)')
        return new_list

    def list_to_database_columns(self):
        new_list = []
        for value in self.fields:
            if value is not None:
                new_list.append(value + ' VARCHAR(255)')
        return new_list

    def list_columns_to_string(self):
        return ' ,'.join(self.get_column_names())