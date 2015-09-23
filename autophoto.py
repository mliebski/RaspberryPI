#!/usr/bin/python

#imports

import time
import RPi.GPIO as GPIO
import picamera
#measurement function

def ranging():
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        start = time.time()

        while GPIO.input(GPIO_ECHO) == 0:
                start = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
                stop = time.time()

        duration = stop - start
        distance = duration * 17150

        return distance

def measure_average():
        #this creates an average of 3 measurements)

        distance1 = ranging()
        time.sleep(0.1)
        distance2 = ranging()
        time.sleep(01.)
        distance3 = ranging()
        distance = distance1 + distance2 + distance3

        distance = distance/3

        return distance

#Main Script

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO = 25

print "Ultraschall Messung"

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.output(GPIO_TRIGGER, False)
camera = picamera.PiCamera()
#main content in block to catch ctrl+c for GPIO cleanup

try:
        while True:
                distance = measure_average()
                if distance <= 60:
                        input_state = GPIO.input(24)
                        print(input_state)
# takes a picture if something is closer than 60 cm to the sensor
                        filename = "image" + str(time.time()) + '.jpg'
                        camera.capture(filename)
                        print("photo taken")
                print "Distance: %.1f" %distance
                time.sleep(3)

except KeyboardInterrupt:
        GPIO.cleanup()
