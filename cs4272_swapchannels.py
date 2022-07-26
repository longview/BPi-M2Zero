#!/usr/bin/python
import spidev, os, time
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 50000
spi.mode = 0

# set ATAPI mode 9 - unswap channels
to_send = [0x20, 0x03, 0b00111001]
retval = spi.xfer3(to_send)
print(retval)
