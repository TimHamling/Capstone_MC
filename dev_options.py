from easygui import *
import sys

addStudent = "/usr/lib/face_recognition/dev_addStudent.py"
deleteStudent = "/usr/lib/face_recognition/dev_deleteStudent.py"
facialRecognition = "/usr/lib/face_recognition/facialRecognition.py"

msg = "Developer Interface"
title = "Manhattan College Facial Recognition Interface"
choices = ["Add Student", "Delete Student", "Run Facial Recognition", "Exit"]
reply = buttonbox(msg, title, choices=choices)

choice = str(reply)

if (choice == "Add Student"):
	exec(open(addStudent).read())

if (choice == "Delete Student"):
	exec(open(deleteStudent).read())

if (choice == "Run Facial Recognition"):
	exec(open(facialRecognition).read())
	
if (choice == "Exit"):
	sys.exit()
