import socket


class Server:

	def __init__(self, port):

		self.port = port

		address = ('', port)
		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.s.bind(address)
		except socket.error:
			print("Could not configure the server")
			return None

	def listen(self):

		recv_data, addr = self.s.recvfrom(4096)

		return recv_data, addr
