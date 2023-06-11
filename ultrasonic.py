import RPi.GPIO as GPIO
from gpiozero import DistanceSensor
GPIO.setmode(GPIO.BOARD)
ultrasonic = DistanceSensor(echo=15, trigger=13)

while True:
    ultrasonic.wait_for_in_range()
    print("In range",ultrasonic.distance)
    