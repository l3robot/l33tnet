from sys import executable
from multiprocessing import Process, Pipe

import subprocess as sub
import signal
import os

from common import common
from server import server
from client import chat
from data import data


def server_process(pipe, port, username):

	serv = server.Server(port)

	print("Listening on port {} ...".format(port))
	print('-'*10)
	print()

	ppid = os.getppid()

	os.kill(ppid, 41)
	
	while True:
		name, message, special = data.check(serv.listen())
		if (name != username):
			if not special:
				pipe.send("+ {} > {}".format(name, message))
			else:
				pipe.send("*** {} ***".format(message))
			os.kill(ppid, 42)

def main():

	port = common.PORT
	username = input("Choose a username : ")

	dark_vader, luke = Pipe()

	p = Process(target=server_process, args=(luke, port, username))
	p.start()

	def pause_handler(signum, frame):
		pass

	def chat_handler(signum, frame):
		print(u'\033[2K\n\033[1A',end='', flush=True)
		print(dark_vader.recv())
		print('{} > '.format(username), end="", flush=True)

	signal.signal(41, pause_handler)
	signal.signal(42, chat_handler)

	signal.pause()

	chat.chat(port, username)

	p.terminate()

if __name__ == "__main__":
	main()