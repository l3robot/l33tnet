from sys import executable
import subprocess as sub

from common import common
from server import server
from client import chat
from data import data

def main():

	nok = True

	while nok:
		side = input("Which side? server:s client:c >> ")

		if side == 's' or side == 'c':
			nok = False
		else:
			print("Incorrect answer, retry.")

	PORT = common.PORT

	if side == 's':
		serv = server.Server(PORT)

		print("Listening on port {} ...".format(PORT))

		while True:
			name, message = data.check(serv.listen())
			print("{} : {}".format(name, message))
	else:
		chat.chat(PORT)

if __name__ == "__main__":
	main()