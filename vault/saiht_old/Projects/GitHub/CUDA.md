---
date: 2024-12-19
---
Is the proprietary programming language used by [[Nvidia]] to program their [[GPGPU]]s. It is the abbreviation of **Compute Unified Device Architecture** in 2006 when introduced, but this abbreviation is now rarely used.

## Ideas 2020
I intended to learn CUDA or a higher abstraction layer TensorFlow during my [[Third Sabbatical]], as written down in the [Machine learning project](https://kreier.github.io/ml/) on GitHub. In 2020 you could get a TensorFlow certificate from Google, by 2024 it does not exist anymore.

![[2024_jetson_nano.jpg]]
## Jetson Nano Developer Kit A02 4GB
I got the [Developer Kit A02](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit) (only one CSI camera interface, the B01 has two) of the [Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano) in early 2020. The hardware has only 128 Maxwell cores ([CUDA Compute Capabilty 5.3](https://www.techpowerup.com/gpu-specs/jetson-nano.c3643)) GPU with 472 GFLOPS at 921 MHz. Support for Maxwell ended 2025. And the latest software provided by Nvidia is an image of Ubuntu 18.04.6 LTS - in 2025 that's 7 years old. Ubuntu itself ended the support in May 2023. Included is:

- Kernel GNU/Linux 4.9.201-tegra
- GNU Compiler Collection 7.5.0 (G++ 7.5.0) from 2019
- NVIDIA Cuda Compiler nvcc 10.3.200
- Jetpack 4.6.1-b110 `sudo apt-cache show nvidia-jetpack`
- Python 3.6.9
- No [OpenCL](https://en.wikipedia.org/wiki/OpenCL) (try fix with PoCL)

And a few years later I started to program a few lines in CUDA actually.
## LLMs on the Jetson Nano in 2025
It was already well known how good parallel architectures like GPUs are for machine learning. As an edge-computing application the Jetson Nano was intended for CNNs with object detection for simple autonomous driving experiments.

ChatGPT made known to the world the possibilities of Large Language models, and maybe a Small Language Model would fit on the Jetson? That's the idea behind a few projects of mine:
- https://kreier.github.io/jetson/
- https://github.com/kreier/llama.cpp-jetson
- https://github.com/kreier/llama.cpp-jetson.nano