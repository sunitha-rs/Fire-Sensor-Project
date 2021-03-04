
import cv2
import json
import requests
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)


# Declarations
# output pins
Servomotor_Pin = 3
#Detected_LED = 16
WIFI_LED = 18
Power_LED = 15


# input pins
IR_Sensor = 7
Power_Switch = 16
WIFI_Switch = 12
Buzzer_LED = 22

Power_Flag = False
WIFI_Flag = False

#_________________________________________________

GPIO.setmode(GPIO.BOARD)

#____________________________________________________

# pin setting

GPIO.setup(Servomotor_Pin,GPIO.OUT) # setting pin output
pwm = GPIO.PWM(Servomotor_Pin,50)# Setting 50 Hzs
pwm.start(0)


#GPIO.setup(Detected_LED,GPIO.OUT)
GPIO.setup(WIFI_LED,GPIO.OUT)
GPIO.setup(Power_LED,GPIO.OUT)
GPIO.setup(Buzzer_LED,GPIO.OUT)


GPIO.setup(IR_Sensor,GPIO.IN) # sensor setup
GPIO.setup(Power_Switch,GPIO.IN,pull_up_down=GPIO.PUD_UP) # power button setup
GPIO.setup(WIFI_Switch,GPIO.IN,pull_up_down=GPIO.PUD_UP) # wifi button setup

#______________________________________________________



def Capturing_images():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        #if key == ord('s'): 
        time.sleep(5)
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        key = cv2.waitKey(2)
        webcam.release()
        cv2.destroyAllWindows()
        print("Image saved!")
        break

def Servomotor_SetAngle(angle):
    duty = angle /18+2
    GPIO.output(3,True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)


def Updating_Images_GoogleDrive():
    headers = {"Authorization": "Bearer ya29.A0AfH6SMAjCe1R2XJzTWHe12b8OhMeCTFMThjAS2OH0I7C94l-I5LhKubfDoFzRWl8QdvYV8NwVcKCd7vImPiYhXR8WRopdKHjcGgrxWS9p66KsRepScrZiEnRcmRy4NFp7OIRJ6zHxU5WzcE2IC7IJqPyjylp"}
    para = {
        "name": "Raspberry_pi.png",
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("./saved_img.jpg", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    print(r.text)

print("program begins")
GPIO.output(Power_LED,GPIO.HIGH)
GPIO.output(WIFI_LED,GPIO.HIGH)
GPIO.output(Buzzer_LED,GPIO.HIGH)
#Servomotor_SetAngle(0)
#pwm.stop()


while True:
    Power_Status = GPIO.input(Power_Switch)
   # if (Power_Status == False):

  #      print("power button on")
    WIFI_Status = GPIO.input(WIFI_Switch)
   # if(WIFI_Status == False):    
       # print("WIFI button on")
    if (Power_Status == False and  WIFI_Status == False): # power button and wifi on condition
	print(" both on")
        if GPIO.input(IR_Sensor): # sensor motion detection
            print("object detected")
            Servomotor_SetAngle(180) # sermo motor i.e camera cap open
            print("in servo motor")
            pwm.stop()
            Capturing_images() # capturing the images
            Updating_Images_GoogleDrive() # updating  image to the google drive
            
        else:
            print("object not detected")


    elif (Power_Status == False and WIFI_Status == True ):# power button on ,wifi off 
            Servomotor_SetAngle(0) # i.e camera cap close
            pwm.stop()
            GPIO.output(Buzzer_LED,GPIO.LOW) # instead of buzzer led used
            time.sleep(1)
            GPIO.output(Buzzer_LED,GPIO.HIGH)
            time.sleep(1)
    else:
        print("check for the power supply") # power not given comes to the else part
        time.sleep(1)
    













