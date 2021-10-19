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
pcf.digitalWrite(LED0, True)
pcf.digitalWrite(LED1, True)
pcf.digitalWrite(LED2, True)
pcf.digitalWrite(LED3, True)

while True:
	pcf.digitalWrite(LED0, False)
	time.sleep(1)
	pcf.digitalWrite(LED1, False)
	time.sleep(1)
	pcf.digitalWrite(LED2, False)
	time.sleep(1)
	pcf.digitalWrite(LED3, False)
	time.sleep(1)
	pcf.digitalWrite(LED0, True)
	pcf.digitalWrite(LED1, True)
	pcf.digitalWrite(LED2, True)
	pcf.digitalWrite(LED3, True)
	time.sleep(1)
