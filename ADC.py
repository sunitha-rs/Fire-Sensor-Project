import RPi.GPIO as GPIO

GPIO.setwarnings(False)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)

while True:
	POT_Value = GPIO.input(8)
	ADC_Value = (POT_Value *5)/1024
	print(" ADC value :",ADC_Value)
	
