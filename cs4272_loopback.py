#!/usr/bin/python
import spidev, os, time
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 50000
spi.mode = 0

# this file configures the codec for digital loopback, intended for use in hardware X-band applications
# the DAC volumes are also changed to set the correct repeat-gain
# note that SA818 and SA818S modules appear to have different transmit gains?

# set ATAPI mode 6 - swap channels
to_send = [0x20, 0x03, 0b00110110]
retval = spi.xfer3(to_send)
print(retval)

# set digital loopback
to_send = [0x20, 0x07, 0b00010010]
retval = spi.xfer3(to_send)
print(retval)

# set volume for X-band
to_send = [0x20, 0x04, 12]
retval = spi.xfer3(to_send)
print(retval)

to_send = [0x20, 0x05, 3]
retval = spi.xfer3(to_send)
print(retval)
