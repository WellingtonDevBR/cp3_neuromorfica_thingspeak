import requests
from decouple import config
from repository.mysql_database import MYSQL
from sensors.air_sensor.air_sensor import AirSensor
from datetime import datetime
from sys import exit

db_instance = MYSQL(
    host=config('MYSQL_HOST'),
    port=config('MYSQL_PORT'),
    username=config('MYSQL_USER'),
    password=config('MYSQL_PASSWORD')
)

db = db_instance.connect()

# AIR SENSOR
response = requests.get(config('URL_AIR_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'AIR'
    air_sensor = AirSensor(response.json())
    columns = air_sensor.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
    data = air_sensor.get_data_from_channel()
    sql = f"INSERT INTO {table_name} (id, temp, humidity, pressure, concentration, pwrsrc, airQuality, created_at ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
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
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")

# AIR POLLUTION SENSOR
response = requests.get(config('URL_AIR_POLUTION_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'AIR_POLUTION'
    air_polution = AirSensor(response.json())
    columns = air_polution.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
    data = air_polution.get_data_from_channel()
    sql = f"INSERT INTO {table_name} (id, Temperature, Humidity, CO_2, created_at ) VALUES (%s, %s, %s, %s, %s)"
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
                object['created_at']
            )
            db_instance.insert_data(sql, val)
        elif (object['entry_id'] > last_registered_id[0]):
            val = (
                object['entry_id'],
                object['field1'],
                object['field2'],
                object['field3'],
                object['created_at']
            )
            db_instance.insert_data(sql, val)
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")

# CO2 SENSOR
response = requests.get(config('URL_CO2_MEASUREMENT_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'CO2_MEASUREMENT'
    co2_measurement_sensor = AirSensor(response.json())
    columns = co2_measurement_sensor.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
    data = co2_measurement_sensor.get_data_from_channel()
    sql = f"INSERT INTO {table_name} (id, eCO2_ppm, eTVOC_ppb, Temperature_C, Air_pressure_3m_asl_hPa, Humidity_H, Controller_temperature_C, G_S, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
                object['field7'],
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
                object['field7'],
                object['created_at']
            )
            db_instance.insert_data(sql, val)
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")

# SHAKES SENSOR
response = requests.get(config('URL_SHAKE_TRAFFIC_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'SHAKE_TRAFFIC'
    shake_sensor = AirSensor(response.json())
    columns = shake_sensor.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
    data = shake_sensor.get_data_from_channel()
    sql = f"INSERT INTO {table_name} (id, Filtered_Results, Sample1, Sample2, created_at ) VALUES (%s, %s, %s, %s, %s)"
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
                object['created_at']
            )
            db_instance.insert_data(sql, val)
        elif (object['entry_id'] > last_registered_id[0]):
            val = (
                object['entry_id'],
                object['field1'],
                object['field2'],
                object['field3'],
                object['created_at']
            )
            db_instance.insert_data(sql, val)
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")

# TEMPERATURE SENSOR
response = requests.get(config('URL_TEMPERATURE_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'TEMPERATURE'
    temperature_sensor = AirSensor(response.json())
    columns = temperature_sensor.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
    data = temperature_sensor.get_data_from_channel()
    sql = f"INSERT INTO {table_name} (id, Temp_C_SALON, Temp_C_OUT, Temp_C_SYPIALNIA, Temp_C__DOMEK_PARTER, Temp_C_DOMEK_STRYCH, Temp_C_BOJLER, Temp_C__NOWY, created_at ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
                object['field7'],
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
                object['field7'],
                object['created_at']
            )
            db_instance.insert_data(sql, val)
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")

# WEATHER SENSOR
response = requests.get(config('URL_WEATHER_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'WEATHER'
    weather_sensor = AirSensor(response.json())
    columns = weather_sensor.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
    data = weather_sensor.get_data_from_channel()
    sql = f"INSERT INTO {table_name} (id, Wind_Direction_North_degrees, Wind_Speed_mph, _Humidity, Temperature_F, Rain_Inchesminute, Pressure_Hg, Power_Level_V, Light_Intensity, created_at ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
                object['field6'],
                object['field7'],
                object['field8'],
                object['created_at']
            )
            db_instance.insert_data(sql, val)
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")


# WIND SENSOR
response = requests.get(config('URL_WIND_POWER_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'WIND'
    wind_sensor = AirSensor(response.json())
    columns = wind_sensor.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
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
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")

# AIR QUALITY SENSOR
response = requests.get(config('URL_AIR_QUALITY_SENSOR'))
if (response.status_code == 200):
    database_name = 'sensors'
    table_name = 'AIR_QUALITY'
    air_quality_sensor = AirSensor(response.json())
    columns = air_quality_sensor.list_columns_to_string()
    is_database_created = db_instance.create_database(database_name)
    is_database_set = db_instance.set_database(database_name)
    is_table_created = db_instance.create_table(table_name, columns)
    if is_table_created != True:
        exit()
    print('Table created')
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
        else:
            print("Nothing to insert")

            pass
else:
    print(f"there's a {response.status_code} error with your request")
