import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#red
red = 27
GPIO.setup(27, GPIO.OUT)
#yellow
yellow = 17
GPIO.setup(17, GPIO.OUT)
#green
green = 18
GPIO.setup(18, GPIO.OUT)

def all_off():
	GPIO.output(red, GPIO.LOW)
	GPIO.output(yellow, GPIO.LOW)
	GPIO.output(green, GPIO.LOW)

### light show
#iterations = 0
def light_show(colors = [17, 18, 27], iterations = 0):
	if iterations < 400:
	#while True:
		act_led = random.choice(colors)
		if (act_led not in leds_on):

			leds_on.append(act_led)
			GPIO.output(act_led, GPIO.HIGH)
		elif (act_led in leds_on):
			leds_on.remove(act_led)
			GPIO.output(act_led, GPIO.LOW)
		iterations += 1
		#return iterations
		print(iterations)
		time.sleep(0.1)
		light_show(iterations=iterations)
	else:	
		all_off()
		print("done")
#GPIO.output(red, GPIO.HIGH)
#GPIO.output(yellow, GPIO.HIGH)
#GPIO.output(green, GPIO.HIGH)

#time.sleep(15)
#all_off()
leds_on = []
#iterations = 0
light_show()

