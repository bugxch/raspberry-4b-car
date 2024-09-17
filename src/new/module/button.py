#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pinconfig import PinConfig
from gpiozero import Button


class CarButton(Button):
    def __init__(self):
        config = PinConfig("config.toml")
        super().__init__(config.button(), pull_up=True)


if __name__ == '__main__':
    button = CarButton()
    print("button pressed {}".format(button.is_pressed))
