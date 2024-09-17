#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from module.motor import CarMotor  # type: ignore


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
