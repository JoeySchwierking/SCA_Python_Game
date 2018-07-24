import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
colors = ['R', 'G', 'B', 'Y']
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
#this script appends a value to a list

def append_list():

	while True:
		n = random.randint(0,3)
		LED.setColor(colors[n])
		time.sleep(0.5)
		LED.noColor()
		time.sleep(0.5)

if __name__ == '__main__':
	try:
		append_list()
	except KeyboardInterrupt:
		print '''Good Grief! I'm out of here.'''