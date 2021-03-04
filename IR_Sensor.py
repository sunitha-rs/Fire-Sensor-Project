import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.IN)

while True:
	val = GPIO.input(3)
	print("val:",val)
