from easygui import *
import os
import shutil
from PIL import Image
import sys
from db_functions import *

msg = "Delete A Student"
title = "Delete a Student"
fieldNames = ["Student ID"]
fieldValues = [] # we start with blanks for the values

known_students = "/usr/lib/face_recognition/Known_Students/"

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

		matchPath = known_students
		mylist = os.listdir(matchPath)

		studentExists = check_id(studentID)

		if (studentExists == False): errmsg = ("Student does not exist.")
		if (studentExists):
			newName = matchPath + "/" + studentID + "_" + get_first(studentID) + "_" + get_last(studentID) + ".jpg"

			try:
				os.remove(newName)
			except OSError:
				pass

			errmsg = "Student " + studentID + " deleted."

			delete_student(studentID)


	fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
	
