
from easygui import *
import os
import shutil
from PIL import Image
import sys
from pymongo import *
from db_functions import *
import face_recognition
import numpy as np

msg = "Add A Student"
title = "Add a Student"
fieldNames = ["Student ID", "First Name", "Last Name"]
fieldValues = [] # we start with blanks for the values
known_students = "/usr/lib/face_recognition/Known_Students"
options = "/usr/lib/face_recognition/dev_options.py"

fieldValues = multenterbox(msg, title, fieldNames)

# Cancel goes back to options menu
if fieldValues is None:
	exec(open(options).read())

while 1:
	
	if fieldValues is None: exec(open(options).read())
	errmsg = ""
	for i in range(len(fieldNames)):
		if fieldValues[i].strip() == "":
			errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])
			
	if errmsg == "":
	
		studentID = str(fieldValues[0])
		firstName = str(fieldValues[1])
		lastName = str(fieldValues[2])

		fixedImageName = studentID + "_" + firstName + "_" + lastName + ".jpg"

		
		matchPath = known_students
		mylist = os.listdir(matchPath)

		if (check_id(studentID)): errmsg = ("Student already exists.")
			
		if errmsg == "":
			
			addStudentImage = fileopenbox(filetypes = ["*.jpg"])
			im = Image.open(addStudentImage)
			width, height = im.size
		
			if (width < 720) or (height < 720): errmsg = ("Invalid Image Size, must be at least 720x720p.")
			
			if errmsg == "":
			
				unknown_image = face_recognition.load_image_file(addStudentImage)
				unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
				
				string_encode = unknown_face_encoding.tostring()
			
				addSplit = addStudentImage.split("/")

				last = len(addSplit) - 1
				path = "";				

				for pathPart in addSplit:
					if pathPart != addSplit[last] and pathPart != "":
						path += "/"
						path += pathPart

				pictureName = addSplit[last]

				newName = path + "/" + studentID + "_" + firstName + "_" + lastName + ".jpg"
				print(newName)
				os.rename(addStudentImage, newName)
				print(addStudentImage)
				destination = known_students
				print(destination)
				shutil.move(newName, destination)
				
				save_id(studentID, firstName, lastName, string_encode)
				print(get_encoding(studentID))

				errmsg = "Student " + studentID + " added."
		
	fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
