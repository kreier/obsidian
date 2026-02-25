---
date: 2019-12-17
---
Probably at the date of our [Robot 2019](https://sites.google.com/ais.edu.vn/robot2019) competition I got the Raspberry Pi 4 with 4 GB of RAM. Some RNN and CNN showed fast object detection times and implied, that a Raspberry Pi might be able to control a self driving robot. Well, that's the idea of 2019.
## Hardware
The [Wikipedia page](https://en.wikipedia.org/wiki/Raspberry_Pi_4) as sufficient information. $55 for the 4 GB model has been a dream ever since, the price has gone up by a lot for quite some time.
### CPU BCM2711 Quadcore [Cortex-A72](https://en.wikipedia.org/wiki/ARM_Cortex-A72)
That's at least 64 bit, even better, the instruction set is now [ARMv8-A](https://en.wikipedia.org/wiki/ARM_architecture_family#64/32-bit_architecture) (as compared to )
## History
Someone is going to expand this part. Some ideas and links.
## 2026-02-13 Mini Server
The machine is running for some time now. The command `tuptime` states that the system is alive since 29/01/26. The Github repository [Homelab](https://kreier.github.io/homelab/) will document it a little better one day. One service that is running is Home Assistant to measure a few ambient parameters. 

I got some Tuya Bluetooth temperature and humidity sensors. With new Bluetooth 5.3 BLE protocol they no longer need a AAA battery like the older Xiaomi sensos I have. Now they can run on a CR2032 battery for years. But the BLE communication has also become more save and encrypted. You can no longer simply connect and get the values by pushing a button.
### Firmware update for Tuya TH05
For just 80k or $3.00 you get a temperature and humidity sensor with display and Bluetooth connection, and the battery is also included. How to update the firmware? Here are two options:
- https://pvvx.github.io/TH-05/
- https://github.com/MakersFunDuck/humidity-temperature-sensor-TH05F
- https://github.com/pvvx/THB2
Unfortunately it states on the first link: "Not recommended for purchase". Battery lasts only half a year? Let's find out!