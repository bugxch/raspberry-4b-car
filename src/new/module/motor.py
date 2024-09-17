#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
* @par Copyright (C): 2024-2024, hunan CLB Tech
* @file         Basic_movement
* @version      V2.0
* @details
* @par History

@author: bugxch
"""
from gpiozero import Motor
from pinconfig import PinConfig
import time


class CarMotor:
    def __init__(self):
        config = PinConfig("config.toml")
        [PWML, LIN1, LIN2] = config.left_motor()
        [PWMR, RIN1, RIN2] = config.right_motor()
        self.motor_left = Motor(
            forward=LIN1, backward=LIN2, enable=PWML, pwm=True)
        self.motor_right = Motor(
            forward=RIN1, backward=RIN2, enable=PWMR, pwm=True)

    def up(self, speed, delay=3):
        self.motor_left.forward(speed)
        self.motor_right.forward(speed)
        time.sleep(delay)

    def down(self, speed, delay=3):
        self.motor_left.backward(speed)
        self.motor_right.backward(speed)
        time.sleep(delay)

    def left(self, speed, delay=3):
        self.motor_left.stop()
        self.motor_right.forward(speed)
        time.sleep(delay)

    def right(self, speed, delay=3):
        self.motor_left.forward(speed)
        self.motor_right.stop()
        time.sleep(delay)

    def stop(self, delay=3):
        self.motor_left.stop()
        self.motor_right.stop()
        time.sleep(delay)


# motor test
if __name__ == '__main__':
    motor = CarMotor()
    basic_speed = 0.4
    turn_speed = basic_speed + 0.1
    try:
        while True:
            motor.down(basic_speed)
            motor.up(basic_speed)
            motor.left(turn_speed)
            motor.right(turn_speed)
            motor.stop()

    except KeyboardInterrupt:
        print("exit")