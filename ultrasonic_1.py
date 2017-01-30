#!/usr/bin/env python
from __future__ import print_function
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER=23
GPIO_ECHO=24

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

def measure():
 GPIO.output(GPIO_TRIGGER,True)
 time.sleep(0.00001)
 GPIO.output(GPIO_TRIGGER,False)
 start=time.time()
 stop=time.time()

 while GPIO.input(GPIO_ECHO)==0:
   start=time.time()
  # print("time start=",start)
 while GPIO.input(GPIO_ECHO)==1:
   stop=time.time()
  # print("stop time=",stop)
 
 elapsed=stop-start
 distance=(elapsed*17150)
 return distance

def average():
  distance1=measure()
  time.sleep(0.1)
  distance2=measure()
  time.sleep(0.1)
  distance3=measure()
  time.sleep(0.1)
  distance=distance1+distance2+distance3
  distance=distance/3
  return distance

#print("Ultrasonic Measurement :")
#print(" At 20 deg")

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)
try:
    while True:
        distance_f=average()
        #print("Distance= ",round(distance_f),"cm")
        if round(distance_f)<10:
            print("...OBSTACLE IS NEAR...")
        time.sleep(0.5)

# Reset GPIO settings
except KeyboardInterrupt():
      GPIO.cleanup()
