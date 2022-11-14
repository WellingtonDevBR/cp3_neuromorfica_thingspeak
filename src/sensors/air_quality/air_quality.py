import requests
from decouple import config
from repository.mysql_database import MYSQL
from datetime import datetime
from sys import exit
from sensors.sensor_implementation import SensorImplementation

db_instance = MYSQL(
    host=config('MYSQL_HOST'),
    port=config('MYSQL_PORT'),
    username=config('MYSQL_USER'),
    password=config('MYSQL_PASSWORD')
)

def save_air_quality_sensor_data():
    # AIR QUALITY SENSOR
    response = requests.get(config('URL_AIR_QUALITY_SENSOR'))
    if (response.status_code == 200):
        database_name = 'sensors'
        table_name = 'AIR_QUALITY'
        air_quality_sensor = SensorImplementation(response.json())
        columns = air_quality_sensor.list_columns_to_string()
        is_database_created = db_instance.create_database(database_name)
        is_database_set = db_instance.set_database(database_name)
        is_table_created = db_instance.create_table(table_name, columns)
        if is_table_created != True:
            exit()
        data = air_quality_sensor.get_data_from_channel()
        sql = f"INSERT INTO {table_name} (id, Air_quality_PM25_gm3, Air_quality_PM1_gm3, Temperature_C, Air_pressure_3m_asl_hPa, Humidity_H, Controller_temperature_C, Sensor_time_offset_s, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
                    object['field7'],
                    object['field8'],
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
                    object['field7'],
                    object['field8'],
                    object['created_at']
                )
                db_instance.insert_data(sql, val)
                print('Data inserted', object['entry_id'])
            else:
                pass
    else:
        print(f"there's a {response.status_code} error with your request")