import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(11,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(13,gpio.OUT)



def forward():
	gpio.output(11,0) #enable
	gpio.output(12,1) # direction
	for i in range(0,100):		
		gpio.output(13,1)
		time.sleep(.5)
		gpio.output(13,0)
		time.sleep(.5)


def hold():
	gpio.output(11,1)
	time.sleep(30)


def back():
	gpio.output(11,0)
	gpio.output(12,0)
	for i in range (0,100):
		gpio.output(13,1)
		time.sleep(.5)
		gpio.output(13,0)
		time.sleep(.5)


while True:

	forward()
	hold()
	back()
	hold()
