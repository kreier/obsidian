---
date: 2025-01-03
---
My planning was a possible multi-GPU machine with the [P100 GPU](https://www.techpowerup.com/gpu-specs/tesla-p100-pcie-16-gb.c2888) as main ingredient. With just 16 GB it has less VRAM than the similar [Tesla P40](https://www.techpowerup.com/gpu-specs/tesla-p40.c2878) but has significant higher memory bandwidth because of HBM2 instead of GDDR5. And after the compute heavy prompt processing is done (not very long before the answer starts) it is memory bandwidth that limits the token generation. There is still some MATMUL going on, but even a CPU is sitting idle waiting for some data to multiply to arrive.

|        Specification        |                  Tesla P40                  |        Tesla P100 (PCIe)        |
|:---------------------------:|:-------------------------------------------:|:-------------------------------:|
| CUDA Cores                  | 3,840 cores                                 | 3,584 cores                     |
| Memory Type                 | GDDR5                                       | HBM2                            |
| Memory Capacity             | 24 GB                                       | 16 GB (common PCIe variant)     |
| Memory Speed / Bandwidth    | ~10,008 MHz effective; ~346 GB/s bandwidth  | ~1,430 MHz; ~720 GB/s bandwidth |
| Memory Bus Width            | 384-bit                                     | 4096-bit (HBM2 wide bus)        |
| Max Power Consumption (TDP) | 250 W                                       | 250 W                           |

The P100 is 267mm long and need some extra space for the fan (120mm for a 120 fan) that therefore does not fit into a Prodesk. This needs a dedicated build.
## Mainboard EVGA Z170 4-way classified - broken
I had seed the mainboard with 4 GPU slots a while ago for 600k, then reoffered at Chotot for 450k because one DIMM and one PCIe are broken. But everything else works, and a newer Z370 Gaming mainboard is 1,800k, significantly more expensive. This is just a hobby.
## CPU i3-6100
Initially I had planned to use a i5-6600 4C/4T 3.9 GHz but the seller of the Z170 mainboard offered a i3-6100 CPU for 250k. The difference? 2C/4T 3.7 GHz, for my use case almost not noticeable, and another cost saving. One day I could upgrade to a 7700K when the prices go down (I lost that confidence early 2026)
## GPU GTX 1060 6GB broken
Only 2 DP output work, the HDMI and one DP are broken. I have some DP-HDMI adapter lying around, so for 1600k a 6GB graphics card makes sense. The similar P104-100 is only 650k, but has no graphics whatsoever. I got one later.
## 2025-01-11 Case Xigmatek Cubi II (E-ATX)
The big mainboard needs a big case. Intended for the larger P100 GPU it now also needed more space for the mainboard. Evaluating some options I landed at the Xigmatek and got it locally at tnc for 1,090k. https://www.tnc.com.vn/case-xigmatek-alpha-cubi-ii-black-en45271.html 
## 2025-01-27 Mining with three GPUs
The intention for the 3 GPUs was to be used for LLMs, but as a benchmark test I also run some mining. Far from being profitable it is a good way to see the whole system maxed out:

![[2025-01-27_mining.png]]