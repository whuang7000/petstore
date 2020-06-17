import connexion
import logging
import copy
import datetime
import os

# In-Memory Database
pets = {
	0: {
		"id": 0,
		"category": {
			"id": 0,
			"name": "Mammal"
		},
		"name": "doggie",
		"photoUrls": ["google.com"],
		"tags": [{
			"id": 0,
			"name": "doggie"
		}],
		"status": "available"
	}
}

inventory = {
	"available": 10,
	"pending": 10,
	"sold": 10
}

orders = {
	
}
 
### Constants
PET_STATUSES = ['available', 'pending', 'sold']

def updatePet(body):
	# Error 400 already handled by Connexion.
	id = body['id']
	if id not in pets:
		return "Pet not found.", 404

	# Business logic for updating pet
	pets[id] = body

	return 'Updated pet.', 200

def addPet(body):
	logging.info(body)
	# Business logic for adding pet
	pets[body['id']] = body
	return "Pet added.", 200

def findPetsByStatus(status):
	for s in status:
		if s not in PET_STATUSES:
			return "Invalid status", 400

	results = []

	for pet in pets.values():
		if pet["status"] in status:
			results.append(pet)

	return results, 200

def findPetsByTags(tags):
	# Error 400 already handled by Connexion
	results = []

	for pet in pets.values():
		for t in pet['tags']:
			if t["name"] in tags:
				results.append(pet)

	return results, 200

def getPetById(petId):
	# Can't return error code 400. https://github.com/zalando/connexion/issues/471
	if petId not in pets:
		return "Pet not found.", 404
	return pets[petId], 200

def updatePetWithForm(petId, body):
	# Error 400 is thrown instead of 405 if there is invalid input.
	logging.info(body)
	if petId not in pets:
		return "Invalid ID", 405
	
	try:
		int(body["name"])
		int(body["status"])
		return "Invalid input.", 405
	except:
		if "name" in body:
			pets[petId]["name"] = body["name"]
		if "status" in body:
			pets[petId]["status"] = body["status"]
		return "Successfully updated.", 200

def deletePet(petId):
	# Error 400 already handled by Connexion.
	if petId not in pets:
		return "Pet not found.", 404
	del pets[petId]
	return "Pet deleted.", 200

def uploadFile(petId, body):
	uploaded_file = connexion.request.files['file']
	uploaded_file.save(os.path.join(os.path.abspath(os.getcwd()), 'tests/assets/hey.jpg'))
	return 200

def getInventory():
	# Error 400 already handled by Connexion.
	return inventory, 200

def placeOrder(body):
	# Error 400 already handled by Connexion.
	temp = copy.deepcopy(body)
	temp['status'] = 'Placed'
	temp['shipDate'] = datetime.date.today()
	temp['complete'] = True
	orders[temp['id']] = temp
	return temp, 200

def getOrderById(orderId):
	# Error 400 already handled by Connexion.
	if orderId not in orders:
		return "Order not found.", 404
	return orders[orderId], 200

def deleteOrder(orderId):
	# Error 400 already handled by Connexion.
	if orderId not in orders:
		return "Order not found.", 404
	del orders[orderId]
	return "Order deleted.", 200
