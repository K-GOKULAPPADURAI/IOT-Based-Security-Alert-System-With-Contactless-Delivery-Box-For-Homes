import subprocess
import smtplib
from email.message import EmailMessage
import pyrebase 

# Configure email settings
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "minorproject002@gmail.com"
receiver_email = "gokulappadurai.k@ckcet.ac.in"
email_password = "bflvgiwtazakvktc"

# Configure Firebase settings
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

# Function to send email notification with image link
def send_notification(subject, body, image_link):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(body)

    msg.add_alternative(f"""
        <!DOCTYPE html>
        <html>
            <body>
                <h2>{body}</h2>
                <img src="{image_link}" alt="Motion Detected" width="640" height="480">
            </body>
        </html>
    """, subtype="html")

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(sender_email, email_password)
        smtp.send_message(msg)

# Main loop
while True:
    user_input = input("Enter 'yes' to capture an image (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    if user_input.lower() == "yes":
        # Capture image using fswebcam
        image_file = "motion.jpg"
        subprocess.run(["fswebcam", image_file])
        print("Image captured")

        # Upload image to Firebase Storage
        storage.child(image_file).put(image_file)
        print("Image uploaded to Firebase Storage")

        # Get the download URL of the image
        image_url = storage.child(image_file).get_url(None)

        # Send email notification with image link
        subject = "Security Alert: Motion Detected"
        body = "Motion has been detected in your home."
        send_notification(subject, body, image_url)

        print("Image removed")
