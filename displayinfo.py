#! /usr/bin/python
# -*- coding: utf-8 -*-


import subprocess
import os
import Adafruit_BMP.BMP085 as BMP085
import sys
import time
import lcddriver
import datetime



sensor = BMP085.BMP085()
#camera = picamera.PiCamera()
got_id = "Office"
got_temp = str(sensor.read_temperature())
got_atm = str(sensor.read_pressure()/100)
got_alt = str(sensor.read_altitude())
got_sea = str(sensor.read_sealevel_pressure()/100)
s = float(open('/sys/class/thermal/thermal_zone0/temp').read())
s = s/1000
got_int_temp = str(s)
#print 'temp = ' + got_temp



#clearing the display
lcd=lcddriver.lcd()
lcd.lcd_clear()

#writing the values
temp_string = "Raumtemp: " + got_temp + " Grad"
baro_string = "Luftdruck: " + got_atm + " hPA"

if sensor.read_temperature() < 15:
        fun_string = "Zieh einen Sweater an! :-|"
if sensor.read_temperature() < 24:
        fun_string = ":-) Super Klasse!"
if sensor.read_temperature() > 24:
        fun_string = ":-( zu warm!!"

time_string = datetime.datetime.strftime(datetime.datetime.now(), '%d-%m-%Y %H:%M')

lcd.lcd_display_string(temp_string, 1)
lcd.lcd_display_string(baro_string, 2)
lcd.lcd_display_string(fun_string, 3)
lcd.lcd_display_string(time_string, 4)
