import RPi.GPIO as GPIO
import time

LCD_RS = 7
LCD_E =8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

LCD_CMD = False
LCD_CHR = True
LCD_WIDTH = 16

LCD_LINE_1 = 0X80
LCD_LINE_2 = 0XC0

E_Pulse = 0.0005
E_Delay = 0.0005


def LCD_init():
    LCD_Byte(0x33,LCD_CMD)
    LCD_Byte(0x32,LCD_CMD)
    LCD_Byte(0x06,LCD_CMD)
    LCD_Byte(0x0C,LCD_CMD)
    LCD_Byte(0x28,LCD_CMD)
    LCD_Byte(0x01,LCD_CMD)
    time.sleep(E_Delay)    


def LCD_Byte(Bits,Mode):
    GPIO.output(LCD_RS,Mode)
    GPIO.output(LCD_D4,False)
    GPIO.output(LCD_D5,False)
    GPIO.output(LCD_D6,False)
    GPIO.output(LCD_D7,False)
    if Bits&0x10 == 0x10:
        GPIO.output(LCD_D4,True)
    if Bits&0x20 == 0x20:
        GPIO.output(LCD_D5,True)
    if Bits&0x40 == 0x40:
        GPIO.output(LCD_D6,True)
    if Bits&0x80 == 0x80:
        GPIO.output(LCD_D7,True)

    LCD_Toggle_Enable()
    
    GPIO.output(LCD_D4,False)
    GPIO.output(LCD_D5,False)
    GPIO.output(LCD_D6,False)
    GPIO.output(LCD_D7,False)
    if Bits&0x01 == 0x01:
        GPIO.output(LCD_D4,True)
    if Bits&0x02 == 0x02:
        GPIO.output(LCD_D5,True)
    if Bits&0x04 == 0x04:
        GPIO.output(LCD_D6,True)
    if Bits&0x08 == 0x08:
        GPIO.output(LCD_D7,True)

    LCD_Toggle_Enable()

def LCD_Toggle_Enable():
    time.sleep(E_Delay)
    GPIO.output(LCD_E,True)
    time.sleep(E_Pulse)
    GPIO.output(LCD_E,False)
    time.sleep(E_Pulse)

def LCD_String(Message,Line):
    Message = Message.ljust(LCD_WIDTH," ")
    LCD_Byte(Line,LCD_CMD)
    for i in range(LCD_WIDTH):
        LCD_Byte(ord(Message[i]),LCD_CHR)



def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LCD_E,GPIO.OUT)
    GPIO.setup(LCD_RS,GPIO.OUT)
    GPIO.setup(LCD_D4,GPIO.OUT)
    GPIO.setup(LCD_D5,GPIO.OUT)
    GPIO.setup(LCD_D6,GPIO.OUT)
    GPIO.setup(LCD_D7,GPIO.OUT)

    LCD_init()

    while True:
        LCD_String("Raspberry pi",LCD_LINE_1)
        LCD_String("Connected",LCD_LINE_2) 
        time.sleep(3)
        LCD_String("PIC",LCD_LINE_1)
        LCD_String("Micro Controller",LCD_LINE_2)

        time.sleep(3)

        


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        LCD_Byte(0x01,LCD_CMD)
        LCD_String("HELLO",LCD_LINE_1)
        GPIO.Cleanup()





        





