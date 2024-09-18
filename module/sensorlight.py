#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gpiozero import LightSensor
from .pinconfig import PinConfig


class LeftLightSensor(LightSensor):
    def __init__(self):
        config = PinConfig()
        super().__init__(config.left_sensor())


class RightLightSensor(LightSensor):
    def __init__(self):
        config = PinConfig()
        super().__init__(config.right_sensor())


if __name__ == "__main__":
    left_light_sensor = LeftLightSensor()
    right_light_sensor = RightLightSensor()
