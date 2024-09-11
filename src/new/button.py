#!/usr/bin/env python
"""
* @par Copyright (C): 2010-2024, hunan CLB Tech
* @file         button
* @version      V2.0
* @details
* @par History

@author: bugxch
"""
# import RPi.GPIO as GPIO
import time
from gpiozero import Button, LED

if __name__ == '__main__':     # Program start from here
    button = Button("GPIO19", pull_up=True) #default to 3.3v
    gLed = LED("GPIO5")
    rLed = LED("GPIO6")
    try:
        rLed.on()
        while True:
            if button.is_pressed:
                time.sleep(0.01)
                gLed.on()
                rLed.off()
            else:
                time.sleep(0.01)
                rLed.on()
                gLed.off()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print("destroy")
