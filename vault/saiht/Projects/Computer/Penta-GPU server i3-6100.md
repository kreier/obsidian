---
date: 2025-01-03
---
The goal for this server was to have a dedicated GPU machine with fast VRAM to increase the inference speed. See [[#History]] below. The planned P100 is not that much faster with HBM2 than my 3070 Ti. The multi GPU solution is more flexible and has ultimately more VRAM.
## Mainboard EVGA Z170 4-way classified - broken
I had seen the mainboard with 4 GPU slots a while ago for 600k, then reoffered at Chotot for 450k because one DIMM and one PCIe are broken. But everything else works, and a newer Z370 Gaming mainboard is 1,800k, significantly more expensive. This is just a hobby.
## CPU i3-6100
Initially I had planned to use a i5-6600 4C/4T 3.9 GHz but the seller of the Z170 mainboard offered a i3-6100 CPU for 250k. The difference? 2C/4T 3.7 GHz, for my use case almost not noticeable, and another cost saving. One day I could upgrade to a 7700K when the prices go down (I lost that confidence early 2026)
## GPU cluster
### GTX 1060 6GB broken
Only 2 DP output work, the HDMI and one DP are broken. I have some DP-HDMI adapter lying around, so for 1600k a 6GB graphics card makes sense. The similar P104-100 is only 650k, but has no graphics whatsoever. I got one later.

```
|----------------.------------------------------------------------------------|
| Device ID      | 1                                                          |
| Device Name    | NVIDIA GeForce GTX 1070                                    |
| Device Vendor  | NVIDIA Corporation                                         |
| Device Driver  | 535.288.01 (Linux)                                         |
| OpenCL Version | OpenCL C 3.0                                               |
| Compute Units  | 15 at 1683 MHz (1920 cores, 6.463 TFLOPs/s)                |
| Memory, Cache  | 8110 MB VRAM, 720 KB global / 48 KB local                  |
| Buffer Limits  | 2027 MB global, 64 KB constant                             |
|----------------'------------------------------------------------------------|
| Info: OpenCL C code successfully compiled.                                  |
| FP64  compute                                         0.223 TFLOPs/s (1/32) |
| FP32  compute                                         6.707 TFLOPs/s ( 1x ) |
| FP16  compute                                         0.112 TFLOPs/s (1/64) |
| INT64 compute                                         1.253  TIOPs/s (1/4 ) |
| INT32 compute                                         2.164  TIOPs/s (1/3 ) |
| INT16 compute                                         6.502  TIOPs/s ( 1x ) |
| INT8  compute                                        23.821  TIOPs/s ( 4x ) |
| Memory Bandwidth ( coalesced read      )                        210.08 GB/s |
| Memory Bandwidth ( coalesced      write)                        219.44 GB/s |
| Memory Bandwidth (misaligned read      )                        150.24 GB/s |
| Memory Bandwidth (misaligned      write)                         67.05 GB/s |
| PCIe   Bandwidth (send                 )                          3.90 GB/s |
| PCIe   Bandwidth (   receive           )                          3.55 GB/s |
| PCIe   Bandwidth (        bidirectional)            (Gen2 x16)    3.51 GB/s |
|-----------------------------------------------------------------------------|
```
### P104-100
Got another one on 2026-02-14 and [tested it's speed](https://github.com/kreier/benchmark/blob/main/gpu/opencl/P104-100.txt) - with GRRD5X even faster than the 1070.

```
|----------------.------------------------------------------------------------|
| Device ID      | 0                                                          |
| Device Name    | NVIDIA P104-100                                            |
| Device Vendor  | NVIDIA Corporation                                         |
| Device Driver  | 535.288.01 (Linux)                                         |
| OpenCL Version | OpenCL C 3.0                                               |
| Compute Units  | 15 at 1733 MHz (1920 cores, 6.655 TFLOPs/s)                |
| Memory, Cache  | 8116 MB VRAM, 720 KB global / 48 KB local                  |
| Buffer Limits  | 2029 MB global, 64 KB constant                             |
|----------------'------------------------------------------------------------|
| Info: OpenCL C code successfully compiled.                                  |
| FP64  compute                                         0.223 TFLOPs/s (1/32) |
| FP32  compute                                         6.657 TFLOPs/s ( 1x ) |
| FP16  compute                                         0.112 TFLOPs/s (1/64) |
| INT64 compute                                         1.434  TIOPs/s (1/4 ) |
| INT32 compute                                         2.238  TIOPs/s (1/3 ) |
| INT16 compute                                         6.660  TIOPs/s ( 1x ) |
| INT8  compute                                        24.369  TIOPs/s ( 4x ) |
| Memory Bandwidth ( coalesced read      )                        282.60 GB/s |
| Memory Bandwidth ( coalesced      write)                        314.01 GB/s |
| Memory Bandwidth (misaligned read      )                        170.19 GB/s |
| Memory Bandwidth (misaligned      write)                         69.88 GB/s |
| PCIe   Bandwidth (send                 )                          0.80 GB/s |
| PCIe   Bandwidth (   receive           )                          0.84 GB/s |
| PCIe   Bandwidth (        bidirectional)            (Gen1 x16)    0.82 GB/s |
|-----------------------------------------------------------------------------|
```
### P106-100
I got this Crypto-GPU already in 2024/11/18 for 500k VND in my D7 neighborhood. It is now the slowest one in the cluster.
```
|----------------.------------------------------------------------------------|
| Device ID      | 2                                                          |
| Device Name    | NVIDIA P106-100                                            |
| Device Vendor  | NVIDIA Corporation                                         |
| Device Driver  | 535.288.01 (Linux)                                         |
| OpenCL Version | OpenCL C 3.0                                               |
| Compute Units  | 10 at 1708 MHz (1280 cores, 4.372 TFLOPs/s)                |
| Memory, Cache  | 6075 MB VRAM, 480 KB global / 48 KB local                  |
| Buffer Limits  | 1518 MB global, 64 KB constant                             |
|----------------'------------------------------------------------------------|
| Info: OpenCL C code successfully compiled.                                  |
| FP64  compute                                         0.151 TFLOPs/s (1/32) |
| FP32  compute                                         4.536 TFLOPs/s ( 1x ) |
| FP16  compute                                         0.076 TFLOPs/s (1/64) |
| INT64 compute                                         0.859  TIOPs/s (1/4 ) |
| INT32 compute                                         1.525  TIOPs/s (1/3 ) |
| INT16 compute                                         4.569  TIOPs/s ( 1x ) |
| INT8  compute                                        16.652  TIOPs/s ( 4x ) |
| Memory Bandwidth ( coalesced read      )                        166.56 GB/s |
| Memory Bandwidth ( coalesced      write)                        175.71 GB/s |
| Memory Bandwidth (misaligned read      )                        108.40 GB/s |
| Memory Bandwidth (misaligned      write)                         44.03 GB/s |
| PCIe   Bandwidth (send                 )                          1.66 GB/s |
| PCIe   Bandwidth (   receive           )                          1.67 GB/s |
| PCIe   Bandwidth (        bidirectional)            (Gen1 x16)    1.65 GB/s |
|-----------------------------------------------------------------------------|
```
## History
### 2025-01-10 Original Plans with P40 and P100
My planning was a possible multi-GPU machine with the [P100 GPU](https://www.techpowerup.com/gpu-specs/tesla-p100-pcie-16-gb.c2888) as main ingredient. With just 16 GB it has less VRAM than the similar [Tesla P40](https://www.techpowerup.com/gpu-specs/tesla-p40.c2878) but has significant higher memory bandwidth because of HBM2 instead of GDDR5. And after the compute heavy prompt processing is done (not very long before the answer starts) it is memory bandwidth that limits the token generation. There is still some MATMUL going on, but even a CPU is sitting idle waiting for some data to multiply to arrive.

|        Specification        |  Tesla P40  | Tesla P100  |
| :-------------------------: | :---------: | :---------: |
|         CUDA Cores          | 3,840 cores | 3,584 cores |
|         Memory Type         |    GDDR5    |    HBM2     |
|       Memory Capacity       |    24 GB    |    16 GB    |
|        Memory Speed         |  1808 MHz   |  1,430 MHz  |
|          Bandwidth          |  346 GB/s   |  720 GB/s   |
|      Memory Bus Width       |   384-bit   |  4096-bit   |
| Max Power Consumption (TDP) |    250 W    |    250 W    |
The P100 is 267mm long and need some extra space for the fan (120mm for a 120 fan) that therefore does not fit into a Prodesk. This needs a dedicated build.
### 2025-01-11 Case Xigmatek Cubi II (E-ATX)
The big mainboard needs a big case. Intended for the larger P100 GPU it now also needed more space for the mainboard. Evaluating some options I landed at the Xigmatek and got it locally at tnc for 1,090k. https://www.tnc.com.vn/case-xigmatek-alpha-cubi-ii-black-en45271.html 
### 2025-01-27 Mining with three GPUs
The intention for the 3 GPUs was to be used for LLMs, but as a benchmark test I also run some mining. Far from being profitable it is a good way to see the whole system maxed out:

![[2025-01-27_mining.png]]

### 2026-02-18 P100 in the cloud
I noticed that I can use a P100 with my 7-year old Kaggle account from early 2019 for free! Here is the link, below the result: https://www.kaggle.com/code/kreier/opencl-benchmark

```
.-----------------------------------------------------------------------------.
| Device ID    0 | Tesla P100-PCIE-16GB                                       |
|----------------'------------------------------------------------------------|
| Device ID      | 0                                                          |
| Device Name    | Tesla P100-PCIE-16GB                                       |
| Device Vendor  | NVIDIA Corporation                                         |
| Device Driver  | 580.105.08 (Linux)                                         |
| OpenCL Version | OpenCL C 3.0                                               |
| Compute Units  | 56 at 1328 MHz (3584 cores, 9.519 TFLOPs/s)                |
| Memory, Cache  | 16269 MB VRAM, 1344 KB global / 48 KB local                |
| Buffer Limits  | 4067 MB global, 64 KB constant                             |
|----------------'------------------------------------------------------------|
| Info: OpenCL C code successfully compiled.                                  |
| FP64  compute                                         3.521 TFLOPs/s (1/3 ) |
| FP32  compute                                         8.915 TFLOPs/s ( 1x ) |
| FP16  compute                                        16.576 TFLOPs/s ( 2x ) |
| INT64 compute                                         1.195  TIOPs/s (1/8 ) |
| INT32 compute                                         3.118  TIOPs/s (1/3 ) |
| INT16 compute                                         9.030  TIOPs/s ( 1x ) |
| INT8  compute                                         1.823  TIOPs/s (1/4 ) |
| Memory Bandwidth ( coalesced read      )                        543.07 GB/s |
| Memory Bandwidth ( coalesced      write)                        594.55 GB/s |
| Memory Bandwidth (misaligned read      )                        302.78 GB/s |
| Memory Bandwidth (misaligned      write)                         90.43 GB/s |
| PCIe   Bandwidth (send                 )                          4.73 GB/s |
| PCIe   Bandwidth (   receive           )                          5.19 GB/s |
| PCIe   Bandwidth (        bidirectional)            (Gen3 x16)    4.60 GB/s |
'-----------------------------------------------------------------------------'
```
Some of the PCIe ports have some limitations. If I use all 4 slots then some get reduced from 16 lanes to only 8. And the P104-100 has only 4 of the 16 lanes connected, while running only Gen1. With 0.84 GB/s we see the maximum of 1 GB/s approaching.

| Generation | x1 (1 Lane) | x4 (4 Lanes) | x8 (8 Lanes) | x16 (16 Lanes) |
|------------|------------:|-------------:|-------------:|---------------:|
| PCIe 1.0   |   0.25 GB/s |     1.0 GB/s |     2.0 GB/s |       4.0 GB/s |
| PCIe 2.0   |   0.50 GB/s |     2.0 GB/s |     4.0 GB/s |       8.0 GB/s |
| PCIe 3.0   |  0.985 GB/s |    3.94 GB/s |    7.88 GB/s |     15.75 GB/s |
| PCIe 4.0   |  1.969 GB/s |    7.88 GB/s |   15.75 GB/s |     31.51 GB/s |
Meanwhile the slower P106-100 has all 16 lanes at Gen1 speed. An updated test on 2026-02-19 delivered up to **3.33 GB/s** - 4x the speed of the P104-100. The GTX 1070 reports x16 bus is slowed down to Gen3 x8 on the Z170 Classified mainboard. Theoretical 7.88 GB/s we indeed measured **5.69 GB/s** for this card.