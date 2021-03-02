#!/usr/bin/env python

#Author: Wahida Hussain
#This program takes a picture using the Pi camera module and names it in date-time format.
#A relay controls LED lights, which is activated right before the Pi camera takes the picture.

#To schedule Crontab to execute this program every hour, add this to Crontab:
# */60 * * * * python3 /home/pi/tempeh_cam.py

import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep
from datetime import datetime, date

led_GPIO = 14 #physical pin 8 (connect to IN2 of relay)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_GPIO, GPIO.OUT)

def set_led(state):
    if state:
        GPIO.output(led_GPIO, False)
    else:
        GPIO.output(led_GPIO, True)

set_led(True) #switch on LED so that camera has enough light

dateTimeObj = datetime.now().strftime("%b %d %Y %H:%M:%S") #for naming of image file

camera = PiCamera()
camera.start_preview(fullscreen=False, window=(200,300,400,500))  #optional
sleep(5) #this gives 5seconds for camera to adjust
camera.capture('/home/pi/tempeh images/'+ dateTimeObj +'.jpg')

set_led(False) #switch off LED

camera.stop_preview() #optional

GPIO.cleanup()
