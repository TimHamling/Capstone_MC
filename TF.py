import os 
import shutil
from PIL import Image
import face_recognition
import sys
from db_functions import *
import numpy as np

known_students = "/usr/lib/face_recognition/Known_Students/"
CV2_Image = "/usr/lib/face_recognition/cv2.jpg"

def facialRecognition():

	addStudentImage = CV2_Image

	im = Image.open(addStudentImage)
	width, height = im.size

	if (width < 720) or (height < 720):
		_id = 0
		msg = 0
		print("Invalid Image Size, must be at least 720x720p.")
		return msg, _id
	
	id_list = get_id_list()

	unknown_image = face_recognition.load_image_file(addStudentImage)
	if face_recognition.face_encodings(unknown_image) == []:
			_id = 0
			msg = 0
			print("No face found in captured image")
			return msg
	unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

	image = []

	for known_id in id_list:
		# get encoding from known image
		
		known_faces = get_encoding(known_id)
		results = face_recognition.compare_faces([known_faces], unknown_face_encoding, tolerance = 0.60)
		
		#print(known_id)
		#print(results)

		if (results[0] == 1):
			_id = known_id
			msg = 1
			print("Face recognized")
			return msg, _id

	if (not image):
		_id = 0
		msg = 0
		print("No match found")
		return msg, _id

		
		
		
		
