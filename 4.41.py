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
SWITCH0 = 7

# Turn off the LED by setting the pin high
pcf.portWrite(0)

# Loop for ever
while True:
	# Read the switch - if it is pressed change the LED outputs
	if (pcf.digitalRead(SWITCH0)):
		pcf.portWrite(5)
		
	if pcf.portRead == 5:
		if (pcf.digitalRead(SWITCH0)):
			pcf.portWrite(10)
	elif pcf.portRead == 10:
		if (pcf.digitalRead(SWITCH0)):
			pcf.portWrite(5)
