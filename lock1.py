import RPi.GPIO as GPIO
import time

relay_pin = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, GPIO.HIGH)  # Set relay initial state to OFF

try:
    while True:
        user_input = input("Enter 'on' to turn the relay ON, or 'off' to turn it OFF: ")
        
        if user_input.lower() == 'on':
            print("Turning relay ON")
            GPIO.output(relay_pin, GPIO.LOW)  # Turn relay ON
        elif user_input.lower() == 'off':
            print("Turning relay OFF")
            GPIO.output(relay_pin, GPIO.HIGH)  # Turn relay OFF
        else:
            print("Invalid input. Please enter 'on' or 'off'.")

except KeyboardInterrupt:
    GPIO.cleanup()
