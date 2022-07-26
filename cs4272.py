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
          # start, auto increment zero, volume A is -26 dB, volume B is -21 dB
to_send = [0x20, 0x81, 0b10101001, 0b1000110, 0b00111001, 26, 21, 0b00010000]
retval = spi.xfer3(to_send)
print(retval)

# implement channel swap by default to fix up the swapping done in hardware
to_send = [0x20, 0x03, 0b00110110]
retval = spi.xfer3(to_send)
print(retval)
# following config, clear PDN
to_send = [0x20, 0x07, 0x02]
retval = spi.xfer3(to_send)
print(retval)
