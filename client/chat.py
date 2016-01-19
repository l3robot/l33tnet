import socket
import json

def broadcast(port, message):

	address = ('<broadcast>', port)

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	except socket.error:
		print("Could not create the broadcast socket")
		return None

	s.sendto(message.encode(), address)

	s.close()

def encode(username, message):

	m = {'l33tnet':True, 'name':username, 'message':message}

	return json.dumps(m)

def chat(PORT):
	
	username = input("Choose a username : ")

	print("Write your messages here!")
	print("=========================")
	print()

	while True:
		message = input("> ")
		broadcast(PORT, encode(username, message))

class Emitter:

	def __init__(self, destination, port):
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		except socket.error:
			print("Failed to create a socket for {}".format(destination))
			return None

		try:
			self.s.connect((destination, port))
		except socket.error:
			print("Failed to connect on {} with port {}".format(destination, port))
			return None

	def send(self, message):
		pass

	def close(self):
		self.s.close()
