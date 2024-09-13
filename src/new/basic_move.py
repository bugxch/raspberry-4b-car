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
import time
from gpiozero import Motor


def t_up(left_motor, right_motor, speed, t_time):
    left_motor.forward(speed)
    right_motor.forward(speed)
    time.sleep(t_time)


def t_stop(left_motor, right_motor, t_time):
    left_motor.stop()
    right_motor.stop()
    time.sleep(t_time)


def t_down(left_motor, right_motor, speed, t_time):
    left_motor.backward(speed)
    right_motor.backward(speed)
    time.sleep(t_time)


def t_left(left_motor, right_motor, speed, t_time):
    left_motor.stop()
    right_motor.forward(speed)
    time.sleep(t_time)


def t_right(left_motor, right_motor, speed, t_time):
    left_motor.forward(speed)
    right_motor.stop()
    time.sleep(t_time)


if __name__ == '__main__':

    PWML = "GPIO18"
    LIN1 = "GPIO22"
    LIN2 = "GPIO27"

    PWMR = "GPIO23"
    RIN1 = "GPIO25"
    RIN2 = "GPIO24"

    motor_left = Motor(forward=LIN1, backward=LIN2, enable=PWML, pwm=True)
    motor_right = Motor(forward=RIN1, backward=RIN2, enable=PWMR, pwm=True)

    basic_speed = 0.25

    try:
        while True:
            t_up(motor_left, motor_right, basic_speed, 3)
            t_down(motor_left, motor_right, basic_speed, 3)
            t_left(motor_left, motor_right, basic_speed, 3)
            t_right(motor_left, motor_right, basic_speed, 3)
            t_stop(motor_left, motor_right, 3)
    except KeyboardInterrupt:
        print("exit")
