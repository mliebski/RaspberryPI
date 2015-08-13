#! /usr/bin/python
# -*- coding: utf-8 -*-
#small little program to create a very simple camera using the PI camera module and a push button
#uses the timestamp to create unique filenames
import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

camera = picamera.PiCamera()

while True:
    input_state = GPIO.input(24)
    if input_state == False:
        filename = 'image' + str(time.time()) + '.jpg'
        camera.capture(filename)
        print('Picture Taken')
        time.sleep(0.2)
