# For full details, please see the tutorial at
# https://www.raspinews.com/blinking-led-on-raspberry-pi-using-python/

import RPi.GPIO as GPIO
import time

LedPin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)

def blink():
    print("Blinking eternally! Press Ctrl+C to kill me.")
    while True:
        GPIO.output(LedPin, GPIO.HIGH) # on
        time.sleep(1)
        GPIO.output(LedPin, GPIO.LOW) # off
        time.sleep(1)

def destroy():
    GPIO.output(LedPin, GPIO.LOW) # off
    GPIO.cleanup() # release the resource

if __name__ == "__main__":
    setup()
    try:
        blink()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, release resources
        destroy()




