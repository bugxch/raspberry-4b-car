#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calibrate the pi car servo
"""
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Outputs a 50% duty cycle PWM single on the 0th channel.
# Connect an LED and resistor in series to the pin
# to visualize duty cycle changes and its impact on brightness.

import board
from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
kit.servo[4].actuation_range = 135
kit.servo[5].actuation_range = 135
# change all of the servo to middle loc
for i in range(180, 120, 10):
    kit.servo[4].angle = i
    time.sleep(0.5)
    # kit.servo[5].angle = i


# # Configure min and max servo pulse lengths
# servo_min = 150  # Min pulse length out of 4096
# servo_max = 600  # Max pulse length out of 4096
# # 辅助功能，使设置舵机脉冲宽度更简单。


# def set_servo_pulse(channel, pulse):
#     pulse_length = 1000000    # 1,000,000 us per second
#     pulse_length //= 60       # 60 Hz
#     print('{0}us per period'.format(pulse_length))
#     pulse_length //= 4096     # 12 bits of resolution
#     print('{0}us per bit'.format(pulse_length))
#     pulse *= 1000
#     pulse //= pulse_length
#     pwm.set_pwm(channel, 0, pulse)


# def set_servo_angle(channel, angle):
#     angle = 4096*((angle*11)+500)/20000
#     pwm.set_pwm(channel, 0, int(angle))


# # 频率设置为50hz，适用于舵机系统。
# pwm.set_pwm_freq(50)
# set_servo_angle(5, 90)  # 底座舵机 90
# set_servo_angle(4, 145)  # 顶部舵机 145

# time.sleep(0.5)
