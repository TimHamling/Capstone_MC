from easygui import *
import os
import shutil
from PIL import Image
import face_recognition
import sys
from db_functions import *
import numpy as np

known_students = "/usr/lib/face_recognition/Known_Students/"

def Upload(reply, choice, title) :
	while 1:
		if reply is None: return None
		errmsg = ""
		addStudentImage = fileopenbox(filetypes = ["*.jpg"])

		if (addStudentImage is None):
			exec(open("usr/lib/face_recognition/facialRecognition.py").read())

		im = Image.open(addStudentImage)
		width, height = im.size

		if (width < 720) or (height < 720): 
			errmsg = ("Invalid Image Size, must be at least 720x720p.")
			reply = buttonbox(errmsg, title, choices=choices)
			choice = str(reply)
			return choice
		
		if errmsg == "":

			id_list = get_id_list()

			unknown_image = face_recognition.load_image_file(addStudentImage)
			unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

			image = []

			for known_id in id_list:

				# print(known_id)
				known_faces = get_encoding(known_id)
				results = face_recognition.compare_faces([known_faces], unknown_face_encoding, tolerance = 0.60)
				# print(results)

				if (results[0] == 1):
					
					known_image = "/usr/lib/face_recognition/Known_Students/" + known_id + "_" + get_first(known_id) + "_" + get_last(known_id) + ".jpg"
					
					image.append(known_image)
					# print("Image appended.")

					# resize matched image
					basewidth = 200
					resized1 = Image.open(known_image)
					wpercent = (basewidth / float(resized1.size[0]))
					hsize = int((float(resized1.size[1]) * float(wpercent)))
					resized1 = resized1.resize((basewidth, hsize), Image.ANTIALIAS)
					resized1.save('resized_image.jpg')
					msg = "Access granted. Match found:" 
					reply = buttonbox(msg, title, image = 'resized_image.jpg', choices=choices)
					choice = str(reply)
					return choice # print first true and exit to save run time

			if (not image):
				msg = "Access Denied. No Match Found" 
				reply = buttonbox(msg, title, choices=choices)
				choice = str(reply)
				return choice # print first true and exit to save run time

			

def Options() :
	exec(open("/usr/lib/face_recognition/dev_options.py").read())
	
def Cancel() :
	sys.exit()



msg = "Manhattan College Facial Recognition"
title = "Manhattan College Facial Recognition"
choices = ["Upload Image of Unknown Student", "Options Menu", "Cancel"]
reply = buttonbox(msg, title, choices=choices)

choice = str(reply)

while True :

	if (choice == "Upload Image of Unknown Student"):
		functChoice = Upload(reply, choice, title)
		
	elif (choice == "Options Menu"):
		functChoice = Options()

	elif (choice == "Cancel"):
		functChoice = Cancel()
		
		
	if functChoice != None :
		choice = functChoice
