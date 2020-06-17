import requests

def test_get_inventory():
	headers = {
	    'api_key': 'asdf1234567890'
	}
	response = requests.get('http://0.0.0.0:8080/store/inventory', headers=headers)
	assert response.status_code == 200

def test_place_order():
	headers = {
		'api_key': 'asdf1234567890',
	    'Content-Type': 'application/json'
	}

	valid_data = '{"id": 1,"petId": 0}'

	response = requests.post('http://0.0.0.0:8080/store/order', headers=headers, data=valid_data)
	assert response.status_code == 200

	invalid_data = '{"id": "string","petId": 0}'

	response = requests.post('http://0.0.0.0:8080/store/order', headers=headers, data=invalid_data)
	assert response.status_code == 400 #Invalid order ID

def test_get_order_by_id():
	headers = {
		'api_key': 'asdf1234567890',
	    'Content-Type': 'application/json'
	}

	valid_data = '{"id": 1,"petId": 0}'

	response = requests.post('http://0.0.0.0:8080/store/order', headers=headers, data=valid_data) #Add Order with ID 1
	
	headers = {
	    'api_key': 'asdf1234567890',
	}

	response = requests.get('http://0.0.0.0:8080/store/order/1', headers=headers)
	assert response.status_code == 200

	response = requests.get('http://0.0.0.0:8080/store/order/9', headers=headers)
	assert response.status_code == 404 # ID not found

def test_delete_order():
	headers = {
		'api_key': 'asdf1234567890',
	    'Content-Type': 'application/json'
	}
	valid_data = '{"id": 2,"petId": 0}'
	response = requests.post('http://0.0.0.0:8080/store/order', headers=headers, data=valid_data) #Add Order with ID 2

	headers = {
	    'api_key': 'asdf1234567890',
	}
	response = requests.delete('http://0.0.0.0:8080/store/order/2', headers=headers)
	assert response.status_code == 200

	response = requests.delete('http://0.0.0.0:8080/store/order/9', headers=headers)
	assert response.status_code == 404 # ID not found
