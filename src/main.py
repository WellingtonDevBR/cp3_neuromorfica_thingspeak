from decouple import config
from repository.mysql_database import MYSQL
from flask import Flask, render_template
from sensors.air.air import save_air_sensor_data
from sensors.air_polution.air_polution import save_air_polution_sensor_data
from sensors.air_quality.air_quality import save_air_quality_sensor_data
from sensors.co2_measurement.co2_mesurement import save_co2_measurement_sensor_data
from sensors.shake_traffic.shake_traffic import save_shake_traffic_sensor_data
from sensors.tempture.tempture import save_temperature_sensor_data
from sensors.weather.weather import save_weather_sensor_data
from sensors.wind_power.wind_power import save_wind_sensor_data

app = Flask(__name__)

@app.route('/update')
def update_database():
    save_air_sensor_data()
    save_air_polution_sensor_data()
    save_air_quality_sensor_data()
    save_co2_measurement_sensor_data()
    save_shake_traffic_sensor_data()
    save_temperature_sensor_data()
    save_weather_sensor_data()
    save_wind_sensor_data()



update_database()






