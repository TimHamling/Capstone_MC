from pymongo import MongoClient, InsertOne
import numpy as np

try:
	client = MongoClient('localhost', 27017)
	
	db = client.known_students
	id_collection = db.student_ids

	print("Connecting to database...")

except:
	print("Unable to connect to the database")

def save_id( id, firstname, lastname, unknown_face_encoding ):

	new_student = { "_id" : id,
			"firstname" : firstname,
			"lastname" : lastname,
			"encoding" : unknown_face_encoding}
		
	try:
		post_id = id_collection.insert_one(new_student)
		student_name = id_collection.find_one({"_id" : id})["firstname"]
		message = True
	except:
		message = False

	return message

def check_id( id ):
	
	try:
		existing_student = id_collection.find_one({"_id" : id})["_id"]
		message = True
	except:
		message = False

	return message

def delete_student( id ):
	try:
		id_collection.delete_one({"_id" : id})
		message = True
	except:
		message = False

	return message

def get_first( id ):
	firstName = id_collection.find_one({"_id" : id})["firstname"]
	return firstName
	
def get_last( id ):
	lastName = id_collection.find_one({"_id" : id})["lastname"]
	return lastName
	
def get_encoding( id ):
	string_encode = id_collection.find_one({"_id" : id})["encoding"]
	encoding = np.fromstring(string_encode,dtype=np.float64)
	encoding = encoding.astype(np.float64)
	return encoding
	
def get_id_list():
	id_list = id_collection.find().distinct("_id")
	return id_list
	


