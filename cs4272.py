#!/usr/bin/python
import spidev, os, time
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 50000
spi.mode = 0

os.system("gpio mode 5 output")
os.system("gpio write 5 0")
time.sleep(0.1)
os.system("gpio write 5 1")
#time.sleep(0.001)

# section 5.2.1, following reset write 0x03 to 0x07
to_send = [0x20, 0x07, 0x03]
retval = spi.xfer3(to_send)
print(retval)
# start, auto increment from register 1
# 1: rates set for 48 kHz @ 12.288 MHz, 24 bit I2S DAC data
# 2: no de-emphasis etc.
# 3: soft ramp, ATAPI mode aR + bL (swapped)
# 4: volume A is -26 dB
# 5: volume B is -21 dB
# 6: ADC dither 16-bit (most software only uses 16 bit data), I2S format, freeze software HPF's to avoid LF phase distortion
to_send = [0x20, 0x81, 0b10101001, 0b1000110, 0b00110110, 26, 21, 0b0011011]
retval = spi.xfer3(to_send)
print(retval)

# following config, clear PDN
to_send = [0x20, 0x07, 0x02]
retval = spi.xfer3(to_send)
print(retval)
