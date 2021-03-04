import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


GPIO.setup(03,GPIO.OUT) # setting pin output
pwm = GPIO.PWM(03,50)# Setting 50 Hzs
pwm.start(0)

def SetAngle(angle):
    duty = angle /18+2
    GPIO.output(03,True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
   # GPIO.output(03,False)
   # pwm.ChangeDutyCycle(0)
SetAngle(180)
pwm.stop()
GPIO.cleanup()



