---
date: 2018-10-01
---
I think I got the Raspberry Pi 3 when working at AISVN in 2018. The original [[Raspberry Pi 1]] was running as a video player for a small 5" monitor, connected to its yellow coax video cable. No audio, but it worked! Later revisions of the Pi1 had this port removed.
## Hardware
Finally a SoC with 64 bit! It took a while until the Raspberry Pi Holdings released a stable 64bit version of the operating system - May 2020. Officially only on 2 February 2022 was [Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS) 64-bit released.
### CPU BCM2837 Cortex A53
This is the same CPU as in my Nvidia Jetson Nano. Being one of the first CPUs implementing the ARMv8-A 64-bit instruction set it left room for optimization and acceleration for later designs like the A72 cores. But 64-bit was supported, and the software had something to work with - each step of the stack takes time. It's still running fine in 2026, some 10 years after the introduction of the Raspberry Pi 3.
## 2024-02-12 Benchmark
After waiting on the shelf for several years I reactivated the Pi to see what it's capable of. The results are part of [my benchmark repository](https://github.com/kreier/benchmark/tree/main/sbc-bench) now. It also has some graphs.

![benchmark](https://raw.githubusercontent.com/kreier/benchmark/refs/heads/main/sbc-bench/single.png)
Good to see that the [[Raspberry Pi 4 with 4 GB RAM]] has not only more RAM, but is measurably faster with the more modern Cortex-A72 cores.
## 2024 Home Assistant
After resting for a while I installed Home Assistant on the machine. With only 1 GB of RAM many use this as the only operating system for this small machine.