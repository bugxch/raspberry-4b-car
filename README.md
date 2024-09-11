# raspberry-4b-car
主要目的是基于树莓派4B，将小车的python2到python3迁移改造，实现各种功能
## 部件配置

下面是树莓派的GPIO引脚映射图

![](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/raspberry_pi_3_model_b_plus_gpio-1024x1024.jpg)

参考这个图，确认不同部件得连线

| 部件 | 功能及示例程序 | Board引脚 | BCM引脚 |
| ---- | -------------- | --------- | ------- |
| 按钮 |                |           |         |
| buzz |                |           |         |
| 舵机 |                |           |         |
| 云台 |                |           |         |

## 任务
- [ ] 参考[Simple Guide to the Raspberry Pi GPIO Header - Raspberry Pi Spy](https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/)确认当前配置的每个部件在树莓派中GPIO的连接方式，填写上面的表格
- [ ] 使用gpiozero和wiringpi改造如下程序
  - [ ] buzzer
  - [ ] button
  - [ ] basic movement
