from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

import RPi.GPIO as GPIO

relay_pin = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, GPIO.HIGH)  # Set relay initial state to OFF

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    action = request.form['action']

    if action == 'on':
        print("Turning relay ON")
        GPIO.output(relay_pin, GPIO.LOW)  # Turn relay ON
    elif action == 'off':
        print("Turning relay OFF")
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn relay OFF

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
