from cv2 import *
from TF import facialRecognition 
from serial import *
from struct import *
from time import sleep
import os
from save_image import *

def get_image():
	retval, im = cam.read()
	return im

cam = VideoCapture(1)
CV2_Image = "/usr/lib/face_recognition/cv2.jpg"
Serial_Connect = "/usr/lib/face_recognition/serialConnect.py"

ramp_frames = 30

ser = Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_95433343933351207031-if00', 9600)

cam.set(3, 1280.)
cam.set(4, 720.)

for i in range(ramp_frames):
	temp = cam.read()

frame = get_image()

imwrite(filename = CV2_Image, img = frame)

del(cam)

result, _id = facialRecognition()

if result:
	save_image(True, _id)
else:
	save_image(False, _id)


sent = ser.write(pack('>B', result))

exec(open(Serial_Connect).read())


