import  RPi.GPIO as GPIO
import time

LED_Blink = 12
SW_PIN = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_Blink,GPIO.OUT) #intiallizing led pin
GPIO.setup(SW_PIN,GPIO.IN,pull_up_down=GPIO.PUD_UP) #intiallizing the switch

while True:
	Switch_Status=GPIO.input(SW_PIN)
	if Switch_Status == True:
		GPIO.output(LED_Blink,GPIO.HIGH)
		time.sleep(1)
	else:
		GPIO.output(LED_Blink,GPIO.LOW)
