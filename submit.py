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

# Define a variable reflecting two states (1010 and 0101)
press = False

# Turn off the LED by setting the pin high
pcf.portWrite(0)

# Loop for ever
while True:
	# If the switch is pressed and LEDs are in state 1010, change state to 0101
	if (pcf.digitalRead(SWITCH0)) and press==False:
		pcf.portWrite(10)
		press = True
		
	# If the switch is pressed and LEDs are in state 0101, change state to 1010	
	elif (pcf.digitalRead(SWITCH0)) and press==True:
		pcf.portWrite(5)
		press = False

	time.sleep(0.2)

# Change in switch state changes the state of the LED pattern
