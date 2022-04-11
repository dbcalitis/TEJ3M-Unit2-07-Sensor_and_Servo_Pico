#####################################
# Created by: Daria Bernice Calitis #
# Created on: April 2022            #
#####################################

# It rotates the servo if the sensor detected a distance less than 50cm.

# Imports for Distance Sensor
import time
import board
import adafruit_hcsr04

# Imports for Servo
import pwmio
from adafruit_motor import servo

# Sets the angle of the servo
angle = 0

# create a PWMOut object on Pin 27.
pwm = pwmio.PWMOut(board.GP27, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo. It also resets the angle to the assigned angle.
my_servo = servo.Servo(pwm)
my_servo.angle = angle

# Sets up the distance sensor.
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP13, echo_pin=board.GP14)

while True:
    print((sonar.distance,))
    
    # Rotates the servo if the detected distance is less than 50 cm.
    if sonar.distance < 50:
      if my_servo.angle <= 0:
        angle += 1
        my_servo.angle = angle
      elif my_servo.angle >= 180:
        angle -= 1
        my_servo.angle = angle
      else:
        angle += 1
        my_servo.angle = angle
 
    time.sleep(0.1)
