from easygui import *
import sys

addStudent = "/usr/lib/face_recognition/admin_addStudent.py"
deleteStudent = "/usr/lib/face_recognition/admin_deleteStudent.py"

msg = "Admin Interface"
title = "Manhattan College Facial Recognition Interface"
choices = ["Add Student", "Delete Student", "Exit"]
reply = buttonbox(msg, title, choices=choices)

choice = str(reply)

if (choice == "Add Student"):
	exec(open(addStudent).read())

if (choice == "Delete Student"):
	exec(open(deleteStudent).read())
	
if (choice == "Exit"):
	sys.exit()
