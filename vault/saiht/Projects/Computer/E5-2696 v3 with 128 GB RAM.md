---
date: 2024-02-20
---
Let's go big! For a little more than a year the ChatGPT revolution is unfolding, and the question lingers "Can I do something like this myself"? Some similar models have been made available for free, so you can run them locally on your own machine. But better models are also bigger. So what do you need? A lot of RAM and a lot of compute power. That's what I went for: an older datacenter CPU with 18 cores and 36 threads for a lot of parallel compute power, and 128 GB DDR3 ECC RAM. Really expensive 10 years ago, surprisingly affordable in early 2024. Here is my setup from 20. February 2024.
## CPU: 18 Cores and 36 Threads
Officially this CPU does not even exist on Intel's website. You can only find some information on Wikipedia, it seems to be a unique model tailored for Amazon. Even Linus Tech Tips made [a video about this CPU](https://youtu.be/xt62JyJo1iU?si=sb8GDrDDdsY6oJ_M) when it was still $4500 USD! Its actually the [E5 2699 v3](https://www.intel.com/content/www/us/en/products/sku/81061/intel-xeon-processor-e52699-v3-45m-cache-2-30-ghz/specifications.html) - this one does exist on the Intel webpage -  but the 2696 I have is OEM made to **also support DDR3** and has a **higher** boost clock of **3.8 GHz** (multiplier 15 instead of 13). See here [on Wikipedia](https://en.wikipedia.org/wiki/List_of_Intel_Xeon_processors_(Haswell-based)#Xeon_E5-2696_v3).
## RAM: 128 GB 1866 ECC
Even more surprising, it's only 350,000 VND per 32 GB DIMM, the total 128 GB cost only 1,400,000 VND or 54 USD. With the price surge at the end of 2025.
## 2024-02-20 Build
I got all the materials form https://vitinhgiaphat.com/ and started assembling. Initially I wanted to unlock more power, frequency etc of the CPU. But in many cases I just ran into the thermal limitation and the 145W power limit.
## 2025-01-16 Water cooling
This idea was lingering for a year now, and I finally placed the order for my first water cooling block. By now the AIOs are reliable and affordable, so I ordered one [VSP VCR-240](https://vsp.vn/tan-nhiet-nuoc-vsp-infinity-liquid-cooler-vcr-240-den.html) at Lazada for 630,000 VND or 24 USD.
## 2025-01-27 Include in mining rig
With so many cores, could it be of use for mining? The good days are long over, but for CPU there is at least Monero left. So I gave it a try:
![[2025-01-27_mining.png]]No, 1200 kH is not a lot. A few years ago 18 cores sound a lot, but in 2025 some i3 get close to that core count. 