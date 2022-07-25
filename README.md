# BPi-M2Zero
Various configs and stuff for Banana Pi M2-Zero

All my testing has been done on ARMbian 21.08.1 with kernel 5.10.60-sunxi (this is available in the community archive).
Note that I found upgrading to newer kernels broke several things including wired ethernet, so I've frozen at this version.

## sun8i-h3-i2s0-codec.dts
It's a (works for me) full duplex stereo I2S slave overlay suitable for a 48 kHz codec chip.
It's your job to configure it properly using some type of interface (I2C, SPI, pin strap).

Can be tested using e.g. 
> alsaloop -C hw:0,1 -P hw:0,0 -t 1000000 -r 48000

to loopback from ADC to DAC

And:
> speaker-test -f1000 -t sine -c 2
to make a sine wave on both channels (in sequence)

The pins on the 40 pin header are: 

PA19: BCK, PA18: LRCLK, PA21: SDATA In (from ADC), PA20: SDATA Out (to DAC)

And as you might already know you can do S/PDIF transmit on PA17, though I haven't tried it myself.

## cs4272.py
Very basic SPI configuration script for a CS4272 codec, add the Armbian SPI overlay and set in armbianEnv.txt:
param_spidev_spi_bus=0 to activate SPI0 with CS0

## pps_pa7.dts
This is just a modified DTS for 1PPS input on the M2Z, it uses PA7 (header pin 29)

## Other notes
Also useful to enable I2C0 and UART2 & 3 overlays. Note that I2C1 can not be used with the above I2S interface, since the pins overlap.
