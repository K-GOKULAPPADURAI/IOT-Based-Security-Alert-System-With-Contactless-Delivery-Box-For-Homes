import pyrebase

# Define your Firebase configuration dictionary
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

# Path to the local image file
local_image_path = "home1.jpg"

# Destination path in Firebase Storage
storage_path = "images/image.jpg"

# Upload the image file to Firebase Storage
storage.child(storage_path).put(local_image_path)

download_url = storage.child(storage_path).get_url(None)

print("Image uploaded successfully!")
print("Download URL:", download_url)
