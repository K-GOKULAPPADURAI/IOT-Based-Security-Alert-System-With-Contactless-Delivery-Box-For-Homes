import gpiozero  # The GPIO library for Raspberry Pi
import time  # Enables Python to manage timing

led = gpiozero.LED(23) # Reference GPIO17

while True:
  led.on() # Turn the LED on
  time.sleep(1)
  led.off() # Turn the LED off
  time.sleep(1)  # Pause for 1 second