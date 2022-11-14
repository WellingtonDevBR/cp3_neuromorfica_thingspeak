import requests
import schedule
import time


def job():
    print('test')
    requests.put('http://localhost:3000/sensor/air/update')
    requests.put('http://localhost:3000/sensor/air-polution/update')
    requests.put('http://localhost:3000/sensor/air-quality/update')
    requests.put('http://localhost:3000/sensor/co2-measurement/update')
    requests.put('http://localhost:3000/sensor/shake-traffic/update')
    requests.put('http://localhost:3000/sensor/temperature/update')
    requests.put('http://localhost:3000/sensor/weather/update')
    requests.put('http://localhost:3000/sensor/wind/update')
    
# you can use seconds too for testing purposes
# you can see the incomming calls in main.py console
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)