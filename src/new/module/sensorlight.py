#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gpiozero import LightSensor
class LightSensorControl(LightSensor):
    def __init__(self, pin):
        super().__init__(pin)