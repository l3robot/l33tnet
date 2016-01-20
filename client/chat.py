import socket
import json
import sys
from time import sleep
from random import shuffle, randint


def quitting(PORT, username, command):
	sys.exit(0)

def helping(PORT, username, command):
	print('List of valid commands:')
	for key, c in commands.items():
		print('/{} or /{} : {}'.format(key, c['shortcut'], c['des']))

def clear(PORT, username, command):
	print(u'\033[2J\033[H',end='', flush=True)
	print('-------------')
	print('** l33tnet **')
	print('-------------')
	print()

def catting(PORT, username, command):
	cats = [
		'(^._.^)ﾉ',
		'(=｀ω´=)',
		'(●ↀωↀ●)',
		'(ﾉ*ФωФ)ﾉ',
		'(ㅇㅅㅇ❀)',
		'₍˄·͈༝·͈˄₎◞ ̑̑ෆ⃛',
		'~(=^･ω･^)ﾍ >ﾟ)))彡'
	]

	for x in range(0, randint(1, 3)):
		shuffle(cats)
		broadcast(PORT, encode(username, 'CAT!!! '+ cats[0]))
		for c in cats:
			print(c)
			sleep(randint(1, 2))


shortcuts = {
	'h' : 'help',
	'q' : 'quit',
	'-' : 'clear',
	'c' : 'cat'
}

commands = {
	'help' : { 'command': helping, 'des' : 'List of commands', 'shortcut' : 'h'},
	'quit' : { 'command': quitting, 'des' : 'Quit application', 'shortcut' : 'q'},
	'clear' : { 'command': clear, 'des': 'Clearing screen', 'shortcut' : '-'},
	'cat' : { 'command': catting, 'des' : '(^._.^)ﾉ', 'shortcut' : 'c'}
}

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
	if command == '':
		return

	if not command in commands:
		if command in shortcuts:
			command = shortcuts[command]
		else:
			print('*** Invalid command {} ***'.format(command)) 

	commands[command]['command'](PORT, username, command)

def chat(PORT, username):

	print('-------------')
	print('** l33tnet **')
	print('-------------')
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
