import RPi.GPIO as GPIO
import time
from flask import Flask, render_template
from flask_ngrok import run_with_ngrok
import pyrebase
import cv2
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when the app is run

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
motion_pin = 11
trig_pin = 13
echo_pin = 15
lock_pin = 16

GPIO.setup(motion_pin, GPIO.IN)
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(lock_pin, GPIO.OUT)

firebaseConfig = {
  'apiKey': "AIzaSyAv8xNEPd0T57rtUgSDH2GE2CKJIdStZQo",
  'authDomain': "iot-project-caf0f.firebaseapp.com",
  'databaseURL': "https://iot-project-caf0f-default-rtdb.firebaseio.com",
  'projectId': "iot-project-caf0f",
  'storageBucket': "iot-project-caf0f.appspot.com",
  'messagingSenderId': "657300165046",
  'appId': "1:657300165046:web:3b2387be3b771e65f47117",
  'measurementId': "G-MJVW6MGK28"
}

firebase = pyrebase.initialize_app(firebaseConfig)
storage = firebase.storage()

cap = cv2.VideoCapture(0)

def motion_detected(channel):
    print("Motion detected!")
    capture_video()
    send_alert_email()
    update_product_status()

def capture_video():
    video_path = "output.mp4"  # Set your desired video output path

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))

    start_time = time.time()
    while(time.time() - start_time < 5):  # Capture video for 5 seconds
        ret, frame = cap.read()
        out.write(frame)

    out.release()
    upload_video(video_path)

def upload_video(video_path):
    storage.child("videos/video.mp4").put(video_path)

def measure_distance():
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()
    pulse_end,pulse_start=1,3
    pulse_duration = pulse_end - pulse_start
    speed_of_sound = 34300  # Speed of sound in cm/s
    distance = (pulse_duration * speed_of_sound) / 2

    return distance

def lock():
    GPIO.output(lock_pin, GPIO.HIGH)

def unlock():
    GPIO.output(lock_pin, GPIO.LOW)

def send_alert_email():
    from_email = "k.gokulappaduraikjgv@gmail.com"  # Set your email address
    to_email = "gokulappadurai.k@ckcet.ac.in"  # Set the recipient's email address
    smtp_server = "smtp.gmail.com"  # Set your SMTP server
    smtp_port = 587  # Set your SMTP port
    smtp_username = "k.gokulappaduraikjgv@gmail.com"  # Set your SMTP username
    smtp_password = "pomymwwvzvxvarrt"  # Set your SMTP password

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = "Motion Detected!"

    image_path = capture_image()
    with open(image_path, "rb") as f:
        image_data = f.read()

    image = MIMEImage(image_data, name="motion.jpg")
    msg.attach(image)

    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(msg)
    smtp.quit()

def capture_image():
    image_path = "motion.jpg"  # Set your desired image output path

    ret, frame = cap.read()
    cv2.imwrite(image_path, frame)
    upload_image(image_path)

    return image_path

def upload_image(image_path):
    storage.child("images/motion.jpg").put(image_path)

def update_product_status():
    distance = measure_distance()
    if distance < 10:
        status = "Present"
    else:
        status = "Not Present"
    return status

@app.route("/")
def index():
    video_url = storage.child("videos/video.mp4").get_url(None)
    image_url = storage.child("images/motion.jpg").get_url(None)
    product_status = update_product_status()
    return render_template("index.html", video_url=video_url, image_url=image_url, product_status=product_status)

@app.route("/toggle_lock/<state>")
def toggle_lock(state):
    if state == "on":
        lock()
    elif state == "off":
        unlock()
    return "Success"

if __name__ == "__main__":
    GPIO.add_event_detect(motion_pin, GPIO.RISING, callback=motion_detected)
    app.run()
