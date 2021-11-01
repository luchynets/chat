import socket
import time
import threading


class Server:
	def __init__(self, ip, port):
		self.ip   = ip
		self.port = port
		self.users = []

	def run_server(self):
		print('Run server... ')

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.ip, self.port))
        
		time.sleep(1)
		print()
		print('Server started on {0}:{1}'.format(self.ip, self.port))

		self.sock.listen(6)
		self.add_user()

	def work(self, conn, username):
		while True:
			data = conn.recv(1024)
			if data:
				self.send(conn, f'{username}: {data.decode("utf-8")}')

	def add_user(self):
		while True:
			conn, addr = self.sock.accept()
			username = conn.recv(1024).decode('utf-8')
			self.users.append((username, conn))
			work = threading.Thread(target = self.work, args = [conn, username])
			work.start()
			self.send(conn, '{0} connected to party!'.format(username))

	def send(self, conn, data):
		for user in self.users:
			if conn != user[1]:
				user[1].send(data.encode('utf-8'))



if __name__ == '__main__':
	server = Server('192.168.56.1', 2007)
	server.run_server()
