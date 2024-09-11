# raspberry-4b-car

主要目的是基于树莓派4B，将小车的python2到python3迁移改造，实现各种功能

## 部件配置

下面是树莓派的GPIO引脚映射图

![](https://image-1258996033.cos.ap-shanghai.myqcloud.com/68747470733a2f2f7777772e72617370626572727970692d7370792e636f2e756b2f77702d636f6e74656e742f75706c6f6164732f323031322f30362f7261737062657272795f70695f335f6d6f64656c5f625f706c75735f6770696f2d3130323478313032342e6a7067?imageSlim)

参考这个图，确认不同部件的GPIO的引脚连线

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
