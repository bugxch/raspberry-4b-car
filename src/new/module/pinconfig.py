import toml


class PinConfig:

    def __init__(self, file_name):
        self.config = toml.load(file_name)

    def buzzer(self):
        return self.config['gpio']['BUZZER']

    def button(self):
        return self.config['gpio']['BUTTON']

    def green_led(self):
        return self.config['gpio']['GREEN_LED']

    def red_led(self):
        return self.config['gpio']['RED_LED']

    def left_motor(self):
        rlt = []
        rlt.append(self.config['gpio']['PWML'])
        rlt.append(self.config['gpio']['LIN1'])
        rlt.append(self.config['gpio']['LIN2'])
        return rlt

    def right_motor(self):
        rlt = []
        rlt.append(self.config['gpio']['PWMR'])
        rlt.append(self.config['gpio']['RIN1'])
        rlt.append(self.config['gpio']['RIN2'])
        return rlt

    def left_sensor(self):
        return self.config['gpio']['GPIO12']

    def right_sensor(self):
        return self.config['gpio']['GPIO16']
