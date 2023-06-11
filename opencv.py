import cv2
import pyrebase

# Firebase configuration
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


# Initialize Pyrebase with the configuration
firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the Firebase Storage service
storage = firebase.storage()

# Create a VideoCapture object to access the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open the camera")
    exit()

# Set the resolution of the camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the output video file
output_file = 'output.avi'

# Define the video codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

# Initialize a counter for the frames
frame_count = 0

# Read and display frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is successfully captured
    if not ret:
        print("Failed to capture frame")
        break

    # Write the frame to the output video file
    out.write(frame)

    # Display the frame in a window named 'Camera Stream'
    cv2.imshow('Camera Stream', frame)

    # Increment the frame counter
    frame_count += 1

    # Break the loop after capturing 5 seconds of video (adjust the value as needed)
    if frame_count == 5 * 20:  # 5 seconds * 20 frames per second
        break

    # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()

# Upload the video file to Firebase Storage
storage.child('videos/output.avi').put(output_file)

# Get the download URL of the uploaded video
download_url = storage.child('videos/output.avi').get_url(None)

print("Video uploaded successfully!")
print("Download URL:", download_url)

# Close any open windows
cv2.destroyAllWindows()
