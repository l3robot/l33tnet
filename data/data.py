import json

def check(data):

	try:
		load_data = json.loads(data.decode())
	except TypeError:
		print("Someone doesn't use json....")
		return None

	try:
		ok = load_data['l33tnet']
	except KeyError:
		return None

	return load_data['name'], load_data['message']
