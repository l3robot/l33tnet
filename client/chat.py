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

def encode(username, message, special=False):

	m = {'l33tnet':True, 'name':username, 'message':message, 'special':special}

	return json.dumps(m)

def command(PORT, username, command):

	if command == 'quit' or command == 'q':
		broadcast(PORT, encode(username, '{} leaved the chat'.format(username), special=True))
		print('*** Quitting ***')
	elif command == 'help' or command == 'h':
		print('List of valid commands:')f
		print(' /help : list of command')
		print(' /quit : disconnect and quit application')
	else:
		print('*** Invalid command {} ***'.format(command))

def chat(PORT, username):

	print("Write your messages here!")
	print("=========================")
	print()

	broadcast(PORT, encode(username, '{} joined the chat'.format(username), special=True))

	while True:
		message = input('{} > '.format(username))

		if len(message) == 0 :
			continue
		if (message[0] != '/'):
			broadcast(PORT, encode(username, message))
		else:
			command(PORT, username, message[1:])

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
