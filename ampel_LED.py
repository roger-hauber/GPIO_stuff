import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#green = 18
GPIO.setup(18, GPIO.OUT)
#yellow = 17
GPIO.setup(17, GPIO.OUT)
#red = 27
GPIO.setup(27, GPIO.OUT)

### Ampel Schaltung 
print("rot")
GPIO.output(27, GPIO.HIGH)
time.sleep(10)
print("yellow")
GPIO.output(27, GPIO.LOW)
GPIO.output(17, GPIO.HIGH)
time.sleep(6)
print("grün")
GPIO.output(17, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)
time.sleep(15)
print("fertig")
GPIO.output(18, GPIO.LOW)
