I should probably add Wi-Fi router, since all of my routers have Wi-Fi built in. And apart from simple GB/s switches and one 2.5 GB/s switch I have only one TP-Link managed switch TL-SG105E (v5 1.0.0 sw 20250710 Rel.71066) that distributes the internet signal to the 4 subnets.
## Asus RT-AX55 - WIFI6
- Software v3.0.0.4.386_52315 2024/10/04
- CPU
- RAM 256 MB DDR3
- Flash 128 MB NAND

This is my first WIFI6 device and the heart of my main network and workstation. In it there is
- [[HP Pro Mini 400 G9]]
- [[Raspberry Pi 4 with 4 GB RAM]] and USB3 NVMe
- [[HP EliteDesk 800 G4 TWR]]

## H3C Magic RT3000 - WIFI6
- Software from China Mobile
- CPU Qualcomm IPQ5000 with NPU (Network Processing Unit) and Dual-core ARM ([Cortex-A53](https://en.wikipedia.org/wiki/ARM_Cortex-A53) with 1 GHz) like https://www.8devices.com/products/cherry 
- RAM 256 MB DDR3L
- Flash 16 MB

For guest and network devices I do not trust yet I have a second WIFI6 network with this 10 USD router. None of the users will see the Chinese user interface. And it does 160 MHz channels! Will there be a future with OpenWRT? This would be great!

## TP-Link Archer C7 v4 - WIFI5
- Software OpenWRT 25.12.1 https://openwrt.org/toh/tp-link/archer_c7 
- Newest original firmware from 2019! https://www.tp-link.com/us/support/download/archer-c7/v4/#Firmware
- CPU Qualcomm Atheros QCA9563 with 775 MHz single core
- RAM 128 MB
- Flash 16 MB
- With OpenWRT runs `btop` and Python
This separate OpenClaw🦞 network is used to explore agentic engineering with local tools. Some machines in here are:
- [[Penta-GPU server i3-6100]]
- [[HP Z600 Workstation]]
- [[Pentium G2030]]
## TP-Link WR1043ND v3 - WIFI4
This model is soo old, but since it's network ports support GB/s I'm using similar models since 2011
- Software OpenWRT 25.12.1 https://openwrt.org/toh/tp-link/tl-wr1043nd
- Original firmware: 2015 https://www.tp-link.com/en/support/download/tl-wr1043nd/v3/#Firmware
- CPU Qualcomm Atheros QCA9558 720 MHz
- RAM 64 MB DDR1
- Flash 8 MB

For some time I used it with DD-WRT v3.0 44715 and earlier (prior to 2020). https://dd-wrt.com/support/router-database/?model=WR1043N(D)_3.x. The main purpose is IOT for these devices:
- [[Raspberry Pi 3 with 1 GB RAM]]
- [[Tanix TX mini]]
- [[MXQ Pro 4K]]

