```
Open Source is Intrinsic to Bitcoin
```
# The bitaxeGamma
bitaxe is a fully open source Bitcoin ASIC miner aimed at decentralizing mining. bitaxeGamma is the 5th major revision of the bitaxe that now includes the BM1370 ASIC from the Antminer S21 Pro

![bitaxeUltra assembled](doc/gamma.png)

## Goals
- **Easy**: Just plug it in and mine Bitcoin over WiFi. No external computer needed.
- **Practical**: low cost, low noise, low power, low maintenance. You can run this at home.
- **ASIC Power**: High efficiency and hashrate, based on the latest and greatest Application Specific Integrated Circuits.
- **Versatile**: Mine to any StratumV1 pool, Lottery mine, Solo mine, Or hack it to do whatever you want.
- **Bitcoin Ethos**: Fully open source, permissionless and decentralized to support the worldwide freedom money.

## ASIC
At the heart of the bitaxeGamma is a BM1370 Bitcoin mining ASIC from the Antminer S21 Pro from Bitmain. It's not open source.

- Bitmain claims the BM1370 has 15 J/TH efficiency. We can get pretty close to that with the BitaxeGamma
- The Antminer S21 Pro has a nominal hashrate of 234 TH/s. There are 3 hashboards with 65 chips each, for a total of 195 chips. The bitaxeGamma has a single one of these chips. That means _about_ 1.2 TH/s per bitaxeGamma. Initial testing looks good!
- The BM1370 is brand new and isn't available individually yet. The best place to get these chips is right out of a S21 Pro.
- The BM1370 has a different footprint and pinout from the BM1368, BM1366, BM1397 and BM1387 in previous bitaxe.

## Current Status
- BitaxeGamma 600 is working well and has been released!
- In addition to higher hashrate, the Gamma also uses more power. Please pay attemtion to hash frequency and voltage settings as it's much easier to overheat, especially when using the stock heatsink and fan.
- BM1370 firmware support has been added to [esp-miner](https://github.com/skot/esp-miner)
- Be sure to check the [HW issues](https://github.com/skot/bitaxe/issues) for known bugs, reworks and errata.
- This is an _advanced_ build! You can do it, but if you're not looking for a project, it might be best to buy one pre-assembled from one of the [many sellers](https://bitaxe.org/legit.html). Check [Skot's method](assembly.md) of hand assembling PCBs.

## PCB Hardware
This repo contains all of the design files for the PCB. [KiCAD](https://www.kicad.org/) software is used. There is a BOM file for all of the components that get soldered to the PCB. 

- Order PCBs from your favorite PCB shop, like [JLCPCB](https://jlcpcb.com), [SeeedStudio](https://www.seeedstudio.com/fusion_pcb.html), or [PCBWay](https://www.pcbway.com)
    - Gerbers are in the `Manufacturing Files` dir. PCBs are 4-layer, 6mil trace/space and 0.3mm hole compatible. 1oz outer / 0.5oz inner layer thickness works well.
    - Make sure to order stencils too. These are the "paste" layers in the gerbers folder. one for top and one for bottom.
- All PCB parts except the ASIC are available from [DigiKey](https://www.digikey.com/en/products) and others. You can find Digikey part numbers on the DK tab of the BOM

## Extra Hardware
There are a few other hardware components that are needed for a complete bitaxe.

- **Heatsink**
	- [40x40mm heatsink and 5V fan](https://www.aliexpress.com/item/2251832861666365.html) from a random AliExpress seller. The fans are crap, but the heatsinks are good.  
- **Fan**
	- You **must** have active cooling on the bitaxe. The heatsink alone is not enough.
	- The Bitaxe has a connector for a 4pin, 5V PWM fan. 40mm square, 20mm thick fans work nicely with the suggested heatsink. Make sure to get a 5V fan! 12V spin, but slowly overheating your Bitaxe..
	- Upgrade your fan with the [Noctua NF-A4x10](https://noctua.at/en/nf-a4x10-5v-pwm) 5V 4-Pin fan for a much more pleasant experience.
- **Thermal compound**
	- Use a good quality thermal compound between the heatsink and ASIC. [Thermal Grizzly Kryonaut](https://www.amazon.com/Thermal-Grizzly-Kryonaut-Grease-Paste/dp/B011F7W3LU) has been known to work well.  
- **Display**
	- Supports 0.91" SSD1306-based I2C OLED Module. [Example Amazon seller](https://www.amazon.com/gp/product/B08ZY4YBHL). Make sure to get the male pins to interface with the Bitaxe PCB. 
- **Power Supply**
	- **5V DC Only!** Anything else will damage the Bitaxe. Be careful and double-check your power supply is 5V. Many other voltage power supplies use the same connector.
	- The power supply needs to supply in excess of 4A (20W) and not drop below 5V. Often times you have to use a power supply rated for 25-30W to get this!
 		- The [Meanwell GST60A05-P1J](https://www.digikey.com/en/products/detail/mean-well-usa-inc/GST60A05-P1J/7703709) at 30 Watts is the cadillac of 5V PSUs and is working well with the Gamma.  
	- The bitaxe uses a 5.5x2.1mm, center-positive barrel jack. 5.5x2.5mm plugs have been known to work.
- **Stand**
	- The PCB has corner mounting holes. You're going to want a stand to mount your Bitaxe. Many excellent 3D printed designs are available.

## Firmware
- The [ESP-Miner](https://github.com/skot/ESP-Miner) has initial support for the BM1370 ASIC. Improvements are ongoing.



### ESP32 Programming Requirements
- As of the bitaxeUltra, all ESP32 programming is done through a USB-C cable and connector on the bitaxe. See [ESP-Miner](https://github.com/skot/ESP-Miner) for more details.

## More Information
- Project page at [bitaxe.org](https://bitaxe.org)
- [Open Source Miners United](discord.gg/osmu) Discord chat
- [building.md](building.md) for PCB ordering tips
- [assembly.md](assembly.md) for assembly tips
