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

@app.route('/sensor/air/update', methods=['PUT'])
def update_air_sensor():
    save_air_sensor_data()
    return 'Air sensor updated'

@app.route('/sensor/air-polution/update', methods=['PUT'])
def update_air_polution_sensor():
    save_air_polution_sensor_data()
    return 'Air polution sensor updated'


@app.route('/sensor/air-quality/update', methods=['PUT'])
def update_air_quality_sensor():
    save_air_quality_sensor_data()
    return 'Air quality sensor updated'


@app.route('/sensor/co2-measurement/update', methods=['PUT'])
def update_co2_measurement_sensor():
    save_co2_measurement_sensor_data()
    return 'CO2 measurement sensor updated'


@app.route('/sensor/shake-traffic/update', methods=['PUT'])
def update_shake_traffic_sensor():
    save_shake_traffic_sensor_data()
    return 'Shake traffic sensor updated'


@app.route('/sensor/temperature/update', methods=['PUT'])
def update_temperature_sensor():
    save_temperature_sensor_data()
    return 'Temperature sensor updated'


@app.route('/sensor/weather/update', methods=['PUT'])
def update_weather_sensor():
    save_weather_sensor_data()
    return 'Weather sensor updated'


@app.route('/sensor/wind/update', methods=['PUT'])
def update_wind_sensor():
    save_wind_sensor_data()
    return 'Wind sensor updated'


if __name__ == '__main__':
    app.run(debug=True, port=3000)
