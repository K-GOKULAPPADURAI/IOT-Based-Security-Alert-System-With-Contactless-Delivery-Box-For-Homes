import subprocess

# Define the path and filename to save the captured image
image_path = "captured_image.jpg"

# Define the command to capture an image using fswebcam
command = "fswebcam -r 1280x720 --no-banner {}".format(image_path)

# Execute the command to capture the image
subprocess.call(command, shell=True)
