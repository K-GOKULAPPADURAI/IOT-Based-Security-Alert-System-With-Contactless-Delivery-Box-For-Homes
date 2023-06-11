from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
import RPi.GPIO as GPIO
import time

# Set the GPIO pin numbers
relay_pin = 17

# Set the GPIO mode and initialize the relay pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Initialize Flask app
app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

# Variable to track the state of the solenoid lock
lock_state = False

def toggle_lock():
    global lock_state
    if lock_state:
        GPIO.output(relay_pin, GPIO.HIGH)
    else:
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(5)  # Keep the solenoid energized for 5 seconds
        GPIO.output(relay_pin, GPIO.HIGH)
    lock_state = not lock_state

@app.route('/')
def home():
    return render_template('index.html', lock_state=lock_state)

@app.route('/toggle')
def toggle():
    toggle_lock()
    return "Lock state toggled"

if __name__ == '__main__':
    app.run()
    GPIO.cleanup()
