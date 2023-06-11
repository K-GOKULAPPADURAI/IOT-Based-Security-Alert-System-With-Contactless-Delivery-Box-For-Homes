import subprocess

# Define the duration of the video recording (in seconds)

# Define the filename and path to save the recorded video
video_path = "recorded_video.avi"

# Define the command to record the video using ffmpeg
command = "ffmpeg -t {} -f v4l2 -i /dev/video0 -c:v libx264 -preset ultrafast {}".format(5, video_path)

# Execute the command to record the video
subprocess.call(command, shell=True)
