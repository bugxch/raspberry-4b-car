#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from car_setup import CarConfig
from gpiozero import Button


class CarButton:
    def __init__(self):
        config = CarConfig("config.toml")
        self.button = Button(config.button(), pull_up=True)

    def is_pressed(self):
        return self.button.is_pressed


if __name__ == '__main__':
    button = CarButton()
    print("button pressed {}".format(button.is_pressed()))
