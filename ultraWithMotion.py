from gpiozero import MotionSensor, DistanceSensor
import time

pir = MotionSensor(4)
ultrasonic = DistanceSensor(echo=18, trigger=17)

while True:
    if pir.motion_detected:
        print("Motion detected")
    distance = ultrasonic.distance
    print(f"Distance: {distance:.1f} cm")
    time.sleep(0.5)
