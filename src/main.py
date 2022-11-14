import time
from logger import get_module_logger
import schedule
from decouple import config
from repository.mysql_database import MYSQL
from sensors.air.air import save_air_sensor_data
from sensors.air_polution.air_polution import save_air_polution_sensor_data
from sensors.air_quality.air_quality import save_air_quality_sensor_data
from sensors.co2_measurement.co2_mesurement import save_co2_measurement_sensor_data
from sensors.shake_traffic.shake_traffic import save_shake_traffic_sensor_data
from sensors.tempture.tempture import save_temperature_sensor_data
from sensors.weather.weather import save_weather_sensor_data
from sensors.wind_power.wind_power import save_wind_sensor_data

def job():
    get_module_logger('main').info('Start job')
    save_air_sensor_data()
    save_air_polution_sensor_data()
    save_air_quality_sensor_data()
    save_co2_measurement_sensor_data()
    save_shake_traffic_sensor_data()
    save_temperature_sensor_data()
    save_weather_sensor_data()
    save_wind_sensor_data()
    get_module_logger('main').info('End job')

# you can use seconds too for testing purposes
# you can see the incomming calls in main.py console
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
