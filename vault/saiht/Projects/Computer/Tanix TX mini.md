---
date: 2018-09-09
---
I got two Tanix TX mini or Tanix TX3 at the end of 2018:

- 29.10.2018 for 574,000 VND
- 09.09.2018 for 596,000 VND

Description: Android Tivi Box TX3 mini -H - BH 2 năm, 2G Ram và 16G bộ nhớ trong ₫ 574,000
## Parameter
The CPU from Amlogic is a Quadcore [Cortex-A53](https://en.wikipedia.org/wiki/ARM_Cortex-A53) (ARMv8-A 64bit), 
2GB RAM DDR3 1066 MHz, Amlogic S905W [https://en.wikipedia.org/wiki/Amlogic](https://en.wikipedia.org/wiki/Amlogic) in 28nm

- CPU: Quad Core 1.2GHz 64bit Cortex-A53
- RAM: 2 GB DDR3 1066 MHz
- GPU: Mali 450 MP3 750 MHz (from 2012, no OpenCL support, OpenGL ES 2.0)
- HDD: eMMC 16GB flash, USB, HDMI

Link from 2020: [https://www.codedbearder.com/posts/mainline-linux-on-tx3-mini/](https://www.codedbearder.com/posts/mainline-linux-on-tx3-mini/)

At the end of 2018 installed Ubuntu 18.04.3 LTS on this machine - in 2024 this build is more than 5 years old. The kernel is 4.19.0-rc7-aml-s9xxx from balbes. Installed on the internal 16GB eMMC (not NAND since not supported by linux kernel) it currently uses 22%. No wifi, but HDMI output works. Graphical interface?

I've been running it since 2020, with some monero crypto mining - but after some time the machine stopped with a red light. Started for short in 2024 - but power supply issues. Cool at 37 degree Celsius. Not sure why it stopped working. Solution January 28th, 2024: it is the power supply 5V 2A that seems to brown out. Got a new one for **45,000 VND**.

As of October 14th, 2020 balbes150 removed support for Amlogic CPUs, so that is the last active build from him. Didn’t notice in 2020.

Intended use in 2020: create a separate HomeKit server to get the Xiaomi humidity Bluetooth sensors connected to HomeKit and integrated on the iPhone. Never went that far. That’s why the Bluetooth dongle on  these boxes exists. RPi4 maybe?
## Update January 28th, 2024

It is the Tanix TX3 mini with an amlogic S905W CPU. Update von ubuntu 18.04 LTS läuft, vier Kerne mit bis zu 1200 MHz und Temperatur um die 40 Grad. Ende Januar 2024 working now with a new power supply. See above.

Instructions to install an Armbian image: [https://blog.toanquan.net/cai-home-assistant-len-tx3-mini/](https://blog.toanquan.net/cai-home-assistant-len-tx3-mini/) 

According to SteeMan it should be possible to build Armbian for this little computer. And the 64bit CPU is **limited to 32bit for some reason**. It only uses 2 Watts while running. How to install:

[https://forum.armbian.com/topic/15950-can-not-find-image-to-download-for-tx3-mini/](https://forum.armbian.com/topic/15950-can-not-find-image-to-download-for-tx3-mini/) 

And it might have the 5.9.0 kernel. Kernels: [https://github.com/ophub/kernel/releases/tag/kernel_stable](https://github.com/ophub/kernel/releases/tag/kernel_stable) 

- 5.4.268
- 5.10.209 
- 5.15.148
- 6.1.75
- 6.6.14

[https://i12bretro.github.io/tutorials/0316.html](https://i12bretro.github.io/tutorials/0316.html) with 5.9.0
[https://github.com/ophub/amlogic-s9xxx-armbian/releases](https://github.com/ophub/amlogic-s9xxx-armbian/releases) with 24.2.0 jammy 22.04.3

- Debian 12 bookworm from 2023/06/10 
- Armbian Lunar Edge (Kernel 6.2.9)

TV box android 13.0 Ram 4G bộ nhớ 32GB WIFI 2.4G&5G hỗ trợ video 4k siêu rõ nét phù hợp giải trí cho cả gia đình h96max **RK3528** for 689,000 VND. With all the trouble not far in price from an N100 PC with **x86** instructions. **That just works. Even with Windows 11.

Or just get a Aqara Hub M1S . Central Controller for 499,000 VND. It works out of the box. What about connecting using Zigbee? Extra controller?

BTW: A few days earlier, on January 11th, I got already a HP mini PC with just 5 Watt power consumption. Great software support, NVMe built in, power source, modern kernels, and starting at 8GB RAM. And I had upgraded to 32 GB DDR4. See [[HP ProDesk 600 G4 mini i5-8500T]]. I will come back to this reasoning in October. As for upgrading the old PC, I got a [[MXQ Pro 4K]]. The box states 16 GB RAM and 256 GB SSD, and that's even the published numbers on the Android 7 kernel. But of course it is not true.
## Update October 25th, 2024
I think it became very fast clear that while 2W is tempting, there are so many limitations with these cheap Linux boxes for 20 dollar. Software update? New kernel? Expand RAM? NVMe? The NVMe support for the Raspberry 5 over 1 (!) lane is still a thing in 2024. And prices?

- [Tanix TX mini 2GB RAM](https://www.lazada.vn/products/hcmtivibox-tanix-tx3-mini-ram-2gb-rom-16gb-i1437450928-s5950685087.html) 16GB eMMC 650,000 VND
- [Pi3 with 1GB RAM](https://www.thegioiic.com/raspberry-pi-3-model-b-bcm2837b0) 1,599,000 VND
- [Pi4 with 4GB RAM](https://www.thegioiic.com/raspberry-pi-4-model-b-4gb) 1,839,000 VND
- [Pi4 with 8GB RAM](https://www.thegioiic.com/raspberry-pi-4-model-b-8gb) 2,560,000 VND
- [Pi5 with 4GB RAM](https://www.thegioiic.com/raspberry-pi-5-4gb) 2,090,000 VND
- [Pi5 with 8GB RAM](https://www.thegioiic.com/raspberry-pi-5-8gb) 2,960,000 VND
- [HP EliteDesk 800 G3 mini 6600T](https://www.chotot.com/mua-ban-may-tinh-de-ban-thanh-pho-thu-duc-tp-ho-chi-minh/119867042.htm) with 8GB RAM 256GB NVMe 2,000,000 VND 5 Watt idle all incl. 

Is this worth your time and effort? 800 has vPro to remote start and monitor, btw. And runs Win11.

And I already have both Pi3 with 1GB RAM and Pi4 with 4 GB RAM. And since