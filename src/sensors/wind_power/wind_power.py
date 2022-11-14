import requests
from decouple import config
from datetime import datetime
from sys import exit
from repository.mysql_database import MYSQL
from sensors.sensor_implementation import SensorImplementation


db_instance = MYSQL(
    host=config('MYSQL_HOST'),
    port=config('MYSQL_PORT'),
    username=config('MYSQL_USER'),
    password=config('MYSQL_PASSWORD')
)

def save_wind_sensor_data():
    # WIND SENSOR
    response = requests.get(config('URL_WIND_POWER_SENSOR'))
    if (response.status_code == 200):
        database_name = 'sensors'
        table_name = 'WIND'
        wind_sensor = SensorImplementation(response.json())
        columns = wind_sensor.list_columns_to_string()
        is_database_created = db_instance.create_database(database_name)
        is_database_set = db_instance.set_database(database_name)
        is_table_created = db_instance.create_table(table_name, columns)
        if is_table_created != True:
            exit()
        data = wind_sensor.get_data_from_channel()
        sql = f"INSERT INTO {table_name} (id, Wind_Speed, Wind_Power_Density_Wattsm2, Wind_Power_Watts, Air_Density_kgm3, Temperature_F, Pressure_mmHg, created_at ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        last_registered_id = db_instance.get_last_row(table_name)
        for object in data:
            object['created_at'] = datetime.strptime(
                object['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            if (last_registered_id == None):
                val = (
                    object['entry_id'],
                    object['field1'],
                    object['field2'],
                    object['field3'],
                    object['field4'],
                    object['field5'],
                    object['field6'],
                    object['created_at']
                )
                db_instance.insert_data(sql, val)
            elif (object['entry_id'] > last_registered_id[0]):
                val = (
                    object['entry_id'],
                    object['field1'],
                    object['field2'],
                    object['field3'],
                    object['field4'],
                    object['field5'],
                    object['field6'],
                    object['created_at']
                )
                db_instance.insert_data(sql, val)
                print('Data inserted', object['entry_id'])
            else:
                pass
    else:
        print(f"there's a {response.status_code} error with your request")
