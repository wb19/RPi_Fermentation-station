#!/usr/bin/env python

#Author: Wahida Hussain
#This program reads the temperature and humidity via a
#DHT11 sensor, then stores this data into a log.

#To schedule Crontab to execute this program every 60 minutes, add this to Crontab:
# */60 * * * * python3 /home/pi/fan_sensor.py

import Adafruit_DHT
from time import sleep
from datetime import datetime, date

# Set sensor type
sensor = Adafruit_DHT.DHT11
 
# Set GPIO sensor is connected to
gpio = 17
 
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
  print('Failed to get reading. Try again!')
  
current_time = datetime.now().strftime("%H:%M:%S")
current_date = date.today().strftime("%d/%B/%Y")
    
#Append a new line to the log
newLog = current_time + ' on ' + current_date + ' Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity) + '\n'
with open('tempeh_log.txt', 'a') as myLog:
    myLog.write('\n')
    myLog.write(newLog)
    myLog.close()
   
with open('/home/pi/tempeh_log.txt', 'r') as file:
    for last_line in file:
        pass
