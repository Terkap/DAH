# Import I/O expander chip library
from DAH import PCF8574

import time

# Setup chip
pcf = PCF8574(address=0x39)

# A variable to store the pin number for the LED
LED0 = 0

# Turn off the LED by setting the pin high
pcf.digitalWrite(LED0, True)

while True:
	pcf.digitalWrite(LED0, False)
	time.sleep(1)
	pcf.digitalWrite(LED0, True)
	time.sleep(1)
