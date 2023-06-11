import cv2
import smtplib
import imghdr
from email.message import EmailMessage
from gpiozero import MotionSensor

# Initialize motion sensor
motion_sensor = MotionSensor(4)

# Configure video recording
video_output = "output.avi"
video_codec = cv2.VideoWriter_fourcc(*"XVID")
video_fps = 20.0
video_resolution = (640, 480)
video_writer = cv2.VideoWriter(video_output, video_codec, video_fps, video_resolution)

# Configure email settings
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "k.gokulappaduraikjgv@gmail.com"
receiver_email = "gokulappadurai.k@ckcet.ac.in"
email_password = "your-email-password"

# Function to send email notification with attached screenshots
def send_notification(subject, body, attachment):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(body)

    with open(attachment, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(sender_email, email_password)
        smtp.send_message(msg)

# Main loop
while True:
    if motion_sensor.motion_detected:
        # Capture video frames and save to output file
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            if ret:
                video_writer.write(frame)
                cv2.imshow("Video", frame)

                # Capture screenshots when motion is detected
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                _, threshold_frame = cv2.threshold(gray_frame, 100, 255, cv2.THRESH_BINARY)
                contours, _ = cv2.findContours(threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Create a copy of contours as a list before iterating
                contours_copy = list(contours)

                for contour in contours_copy:
                    if cv2.contourArea(contour) > 5000:
                        (x, y, w, h) = cv2.boundingRect(contour)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

                        # Check if there is a human detected
                        # You can implement a machine learning or deep learning model here

                        # Save screenshot
                        screenshot_file = "screenshot.jpg"
                        cv2.imwrite(screenshot_file, frame)

                        # Send email notification with screenshot
                        subject = "Security Alert: Motion Detected"
                        body = "Motion has been detected in your home."
                        send_notification(subject, body, screenshot_file)

                cv2.imshow("Motion Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        video_capture.release()
        video_writer.release()
        cv2.destroyAllWindows()
