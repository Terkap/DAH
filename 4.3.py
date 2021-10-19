# Import I/O expander chip library
from DAH import PCF8574

import time

# Setup chip
pcf = PCF8574(address=0x38)

# A variable to store the pin number for the LED
LED0 = 0
LED1 = 1
LED2 = 2
LED3 = 3


# Turn off the LED by setting the pin high
pcf.portWrite(10)
#print(help(pcf.portWrite))
time.sleep(5)

while True:
	pcf.portWrite(5)
	time.sleep(1)
	pcf.portWrite(10)
	time.sleep(1)
