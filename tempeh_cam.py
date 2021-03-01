#!/usr/bin/env python

#Author: Wahida Hussain
#This program takes a picture using the Pi camera module and names it in date-time format.

#To schedule Crontab to execute this program every hour, add this to Crontab:
# */60 * * * * python3 /home/pi/tempeh_cam.py

from picamera import PiCamera
from time import sleep
from datetime import datetime, date

dateTimeObj = datetime.now().strftime("%b %d %Y %H:%M:%S")
camera = PiCamera()
#camera.start_preview(fullscreen=False, window=(100,200,300,400))  #optional
sleep(5) #this gives 5seconds for camera to adjust
camera.capture('/home/pi/tempeh images/'+ dateTimeObj +'.jpg')
#camera.stop_preview() #optional
