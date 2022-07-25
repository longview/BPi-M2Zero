#!/usr/bin/python
import spidev, os, time
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 50000
spi.mode = 0

# this script configures a CS4272 for I2S master mode at 48 kHz using a 12.288 MHz MCLK
# note that the ATAPI modes may not be entirely correct, see the datasheet.

# change this to whatever is the RESET_L line for the codec
# or remove, it *should* work without resetting for SPI mode
os.system("gpio mode 5 output")
os.system("gpio write 5 0")
time.sleep(0.1)
os.system("gpio write 5 1")
#time.sleep(0.001)

# section 5.2.1, following reset write 0x03 to 0x07
to_send = [0x20, 0x07, 0x03]
retval = spi.xfer3(to_send)
print(retval)
          # start, auto increment zero,
to_send = [0x20, 0x81, 0b10101001, 0b1000110, 0b00111001, 0x0, 0x0, 0b00010000]
retval = spi.xfer3(to_send)
print(retval)
# following config, clear PDN
to_send = [0x20, 0x07, 0x02]
retval = spi.xfer3(to_send)
print(retval)
