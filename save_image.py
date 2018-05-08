from time import *
from datetime import *
import os

def save_image(result, _id):
	time = current_time()
	if result:
		image_name = time + "_" + _id + '_pass.jpg'
	else:
		image_name = time + "_fail.jpg"
	
	images = os.listdir('/usr/lib/face_recognition/Recent_Captures')
	if len(images) >= 100:
		images = sorted(images)
		os.remove('/usr/lib/face_recognition/Recent_Captures/' + images[0])
	
	os.rename('/usr/lib/face_recognition/cv2.jpg', '/usr/lib/face_recognition/Recent_Captures/' + image_name)
	
	

def current_time():
	return datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
