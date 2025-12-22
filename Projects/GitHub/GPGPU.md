A **General Purpose Graphics Processing Unit** ([[GPGPU]]) is a GPU that has additional features to use the large parallel processing power of a GPU for other purposes than rendering graphics. It became useful for machine learning and neuronal networks.
## AlexNet
One breakthrough application was the use of GPUs for image classification with [AlexNet](https://en.wikipedia.org/wiki/AlexNet) in 2016. It significantly increased the accuracy in the [ImageNet](https://en.wikipedia.org/wiki/ImageNet "ImageNet") Large Scale Visual Recognition Challenge (ILSVRC). And the [[Nvidia]] GPUs were programmed with [[CUDA]].

I followed some development of [GPT-1](https://en.wikipedia.org/wiki/GPT-1) in 2017, then [GPT-2](https://en.wikipedia.org/wiki/GPT-2) in 2019 and even [GPT-3](https://en.wikipedia.org/wiki/GPT-2) in 2020. But other than some academic curiosity the real potential and impact was not obvious. And the later models were already out of reach for consumers with the hardware requirements, not just for training, but even for inference.
## LLMs
![[2025-01_server.jpg]]
Ever since OpenAI published ChatGPT in November 2022 the big wave of AI has held the world captive. By **2023** some models were made available to run on local hardware. I remember running a quantized 4b model on my MacBook Pro with 8 GB RAM in early 2023. Still more a "prove of concept", but an interesting one.

- [https://kreier.github.io/ml/](https://kreier.github.io/ml/)

In **2024** I tried to build a server with many cores, the [E5 2696 v3](https://en.wikipedia.org/wiki/LGA_2011) on the LGA 2011 socket with 18 cores and 36 threads. It does run, and 128 GByte EEC RAM are nice. But I soon realized that for inference the key parameter is memory bandwidth. Some 1.5 years later the impact reached the market when prices for DDR5 for consumers skyrocketed.

#### Higher memory bandwidth - GPU again
It was again the GPUs that helped speed up computing here. But in this case it was not related to the massive parallelism of computations, but the general **fast memory bus** these GPUs have. Another detail important for games proved to be helpful for machine learning. 

So in early 2025 I got some used graphics cards to use them in parallel and split the layers of the LLM on different cards. The old crypto boom proved to be helpful in this instance. Nvidia had released some crippled graphics cards that were not very useful to be used as graphics cards. For example they had no HDMI or DP output. The PCIe interface was only 1.0 x4, where comparable graphics cards have PCIe 3.0 x16 - some 16x faster!

- GTX 1070, 1920 CUDA cores, 256 GB/s, 8GB, PCIe 3.0 x16 [link](https://www.techpowerup.com/gpu-specs/geforce-gtx-1070.c2840)
- P104-100, 1920 CUDA cores, 320 GB/s, 8GB, PCIe 1.0 x4 [link](https://www.techpowerup.com/gpu-specs/nvidia-p104-100-8-gb.b8158)
- P106-100, 1280 CUDA cores, 192 GB/s, 6GB, PCIe 1.0 x4 [link](https://www.techpowerup.com/gpu-specs/p106-100.c2980)

Combined this machine has 22 GByte VRAM with up do 320 GB/s bandwidth. Uploading all layers to VRAM is another challenge, there is some overhead. You can't just have a quantized 20 GByte model uploaded to the graphics cards and assume ollama will use all of them.
