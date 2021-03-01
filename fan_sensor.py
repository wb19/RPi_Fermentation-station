#!/usr/bin/env python

#Author: Wahida Hussain
#This program uses the Adafruit library to allow a DHT11 temperature and humidity
#sensor to take readings. The logic: if the temperature exceeds X'Celcius, the fan
#will be turned on for Y seconds.

#To schedule Crontab to execute this program every 10 minutes, add this to Crontab:
# */10 * * * * python3 /home/pi/fan_sensor.py

import RPi.GPIO as GPIO
import Adafruit_DHT
from time import sleep
from datetime import datetime, date

fan_GPIO = 4 #We use 7th physical pin (GPIO 4) to control the fan
GPIO.setmode(GPIO.BCM)
GPIO.setup(fan_GPIO, GPIO.OUT)

# Set sensor type
sensor = Adafruit_DHT.DHT11
# We will use the 11th physical pin (GPIO 17) to read data from sensor
sensor_GPIO = 17
humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_GPIO)

def set_fan(state):
    if state:
        GPIO.output(fan_GPIO, False)
    else:
        GPIO.output(fan_GPIO, True)

#the fan will be activated if the temperature is more than 32'C.
if (temperature >= 32):
    set_fan(True)
    sleep(300)   #fan is activated for n seconds. 300secs = 5mins
else:
    set_fan(False)

current_time = datetime.now().strftime("%H:%M:%S")
current_date = date.today().strftime("%d/%B/%Y")
   
#Append a new line to the log
newLog = current_time + ' on ' + current_date + ' Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity) + '\n'
with open('tempeh_log.txt', 'a') as myLog:
    myLog.write('\n')
    myLog.write(newLog)
    myLog.close()
   
with open('/home/pi/tempeh_log.txt', 'r') as file:
    for last_line in file:
        pass

GPIO.cleanup()
