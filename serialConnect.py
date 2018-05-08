import serial

cv2Capture = "/usr/lib/face_recognition/cv2Capture.py"

ser = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_95433343933351207031-if00', 9600)

while(True):
	if ser.readline() != None:
		exec(open(cv2Capture).read())
	
