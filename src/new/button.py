#!/usr/bin/env python
"""
* @par Copyright (C): 2010-2020, hunan CLB Tech
* @file         button
* @version      V2.0
* @details
* @par History

@author: zhulin
"""
# import RPi.GPIO as GPIO
import time
from gpiozero import Button, LED


# def setup():
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
#     GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
#     GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
#     GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)


if __name__ == '__main__':     # Program start from here
    button = Button("GPIO19", pull_up=True) #default to 3.3v
    gLed = LED("GPIO5")
    rLed = LED("GPIO6")
    try:
        while True:
            if button.is_pressed:
                time.sleep(0.01)
                gLed.off()
                rLed.on()
            elif button.is_released:
                time.sleep(0.01)
                rLed.off()
                gLed.on()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print("destroy")
