#
# Designlapp 2018
#

import RPi.GPIO as GPIO
import time
import os

def gpio_callback(pin):
	''' Callback from GPIO'''
	print("shut down")
	os.system("poweroff")

if __name__ == "__main__":
	''' Run if main '''
	#SETUP
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
	#Detection
	print("starting detection")
	GPIO.add_event_detect(2, GPIO.FALLING, callback = gpio_callback, bouncetime = 200)
	#Keep Running
	while 1:
		time.sleep(1)