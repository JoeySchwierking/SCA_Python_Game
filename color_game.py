import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random
GPIO.setwarnings(False)

R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)
#this script appends a value to a list

def append_list():
	g = 0
	colors = []
	while True:
		time.sleep(1)
		n = random.randint(0,3)
		g = g + 1
		if n == 0:
			a = 'R'
		elif n == 1:
			a = 'G'
		elif n == 2:
			a = 'B'
		elif n == 3:
			a = 'Y'
		colors.append(a)
		color_string = ''.join(colors)
		i = 0
		loop = False
		while loop == False:
			LED.setColor(colors[i])
			time.sleep(0.5)
			LED.noColor()
			time.sleep(0.5)
			i = i + 1
			if i == g:
				loop = True

if __name__ == '__main__':
	try:
		append_list()
	except KeyboardInterrupt:
		print '''ookies? Good Grief! I'm out of here.'''
		LED.destroy()
