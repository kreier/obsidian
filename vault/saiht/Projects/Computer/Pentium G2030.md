---
date: 2021-12-15
---
While tutoring I was asked by my student about the viability of Cryptocurrency and crypto mining. I had heard about it in 2008 and didn't pay much attention back then. Several other attempts like "webcoin" had crashed or gotten nowhere - why should Bitcoin be different?

I soon realized that in 2021 with a CPU you could still generate income, and I had a RX470 with 4 GB lying around. I got it for Machine Learning in 2018 and it was cheap because the crypto boom 2016/2017 was over. Well, here we are 3 years later. 4 GB is a tough limit for DAG size, but I will learn this later.
## Dedicated mining machine
Prior to a dedicated machine I was just using my old [[HP Z600 Workstation]] with the RX470 in it. But the Dual-Xeon consumes a lot of power (150 Watt idle), and I want to work as well, not just mine coins. 2GB VRAM of my GTX 960 was too little for mining (DAG size) but fine for anything work. I swapped the GPU and I got an old mainboard with CPU, cooler and 4 GB of DDR3 RAM for 1m VND or $40 to run with the **RX 470 4GB**
## OS: HiveOS
Instead of starting from an SSD or HDD I started from a USB flash drive. Once it is started the main workload is transferred to the GPU and it just keeps crunching numbers.
## Crypto-GPU: AMD RX470 4GB
For almost 2 years this GPU was mining a few Ravencoins. In 2022 and 2023 it almost broke even with the electricity cost put into it. For the future? Nobody knows. The time when a Ravencoin was above 10 cents are long gone.

Early 2026 the RX 470 moved to the [[E5-2696 v3 with 128 GB RAM]] for Davinci Resolve. With a repaired mainboard it could run without a dedicated GPU just fine. A few weeks later my P106-100 began working again, so the machine was brought back to life.
## AI-GPU: Nvidia P106-100
This is the first crypto-GPU I got, and after a few months it just stopped working, was not detected by the mainboard. Since I only paid 500k I did not considered it a big loss.

After visiting RE COM to possibly fix it they stated 250k fixing costs. I did not want to spend that money, took it back home, and put it back into the G2030 machine - it worked again! Now its in a corner connected over Wifi to run smaller models. I have to update my [[Hardware collection]].

![[liquid.png]]
## LFM2-8B-A1B-GGUF
This model should run the 8B parameter model in Q4-K_M and 5.04 GB. I still have to try.

- Link HF: https://huggingface.co/LiquidAI/LFM2-8B-A1B-GGUF

The promised performance sounds promising. And 8B is the smallest MoE model I could find currently:

![[lfm2_family.png]]