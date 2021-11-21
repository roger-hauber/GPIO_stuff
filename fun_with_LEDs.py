import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("the LED is on! Check it out!")
GPIO.output(18,GPIO.HIGH)
time.sleep(5)
print ("wasnt that cool")
GPIO.output(18, GPIO.LOW)
