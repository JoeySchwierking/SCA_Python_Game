import RPi.GPIO as GPIO
import LEDRGB as LED
import time
import random

# breadboard setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

# assign the RGB LED pin numbers
R_pin = 11
G_pin = 12
B_pin = 13
LED.setup(R_pin, G_pin, B_pin)

# set Passive Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)
Buzz = GPIO.PWM(buzz_pin,1000)

#this script appends a value to a list
def append_list():
	g = 0
	colors = []
	frequencies = []
	while True:
		time.sleep(1)
		n = random.randint(0,3)
		g = g + 1
		if n == 0:
			a = 'R'
			b = 220
		elif n == 1:
			a = 'G'
			b = 440
		elif n == 2:
			a = 'B'
			b = 880
		elif n == 3:
			a = 'Y'
			b = 1760
		colors.append(a)
		frequencies.append(b)
		color_string = ''.join(colors)
		i = 0
		loop = False
		while loop == False:
			LED.setColor(colors[i])
			Buzz.ChangeFrequency(frequencies[i])
			Buzz.start(50)
			time.sleep(0.5)
			LED.noColor()
			Buzz.stop()
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
