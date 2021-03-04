import serial
ser = serial.Serial('/dev/ttyS0',9600,timeout=10)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')
while True:
	data=input("write something\n\r")
	write1=ser.write(str.encode(data))
	print("waiting for the response")
	line = ser.readlines()
	print("line read",line)
