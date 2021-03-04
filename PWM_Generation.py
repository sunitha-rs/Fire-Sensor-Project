import RPi.GPIO as GPIO
import time
LED_BLINK = 8
LED_PWM = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(LED_BLINK,GPIO.OUT)
GPIO.setup(LED_PWM,GPIO.OUT)



PWM=GPIO.PWM(LED_PWM,100)
PWM.start(0)

while True:
    GPIO.output(LED_BLINK,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_BLINK,GPIO.LOW)
    time.sleep(1)

    for i in  range(100):
        PWM.ChangeDutyCycle(i)
        time.sleep(0.1)
