from easygui import *

admin_options = "/usr/lib/face_recognition/admin_options.py"
dev_options = "/usr/lib/face_recognition/dev_options.py"

msg = "Admin & Dev Logon"
title = "Manhattan College Facial Recognition Login"
fieldNames = ["User ID","Password"]
fieldValues = []
# we start with blanks for the values
fieldValues = multpasswordbox(msg,title, fieldNames)
# make sure that none of the fields was left blank
while 1:
	if fieldValues is None: break
	errmsg = ""
	for i in range(len(fieldNames)):
		if fieldValues[i].strip() == "":
			errmsg += ('"%s" is a required field.\n\n' % fieldNames[i])
		if ((fieldValues[0].strip() != "admin") or (fieldValues[0].strip() != "dev")) and (fieldValues[1].strip() != "password") :
			errmsg = ("Invalid login, try again.")
	if errmsg == "":
		break # no problems found
	fieldValues = multpasswordbox(errmsg, title, fieldNames, fieldValues)

userID = str(fieldValues[0])
password = str(fieldValues[1])

print(userID, password)

if (userID == "admin") and (password == "password"):
	print("Admin Success.")
	exec(open(admin_options).read())
elif (userID == "dev") and (password == "password"):
	print("Developer Success.")
	exec(open(dev_options).read())



