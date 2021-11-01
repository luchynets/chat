import socket
import threading


class Client:
	def __init__(self, ip, port):
		self.ip   = ip
		self.port = port

		
	def connect(self, username):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.ip, self.port))
		self.sock.send(username.encode('utf-8'))

		send = threading.Thread(target = self.send)
		send.start()

		self.get_data()

	def send(self):
		while True:
			self.sock.send(input('Enter the message --> \n').encode('utf-8'))

	def get_data(self):
		while True:
			data = self.sock.recv(1024).decode('utf-8')
			print(data)


if __name__ == '__main__':
	print('''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╭━╮╭━╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱┃┃╰╯┃┃
┃┃╱┃┣━╮╭━━┳━╮╭┳╮╭┫╭╮╭╮┣━━┳━━┳━━┳━━┳━╮╭━━┳━━┳━╮
┃╰━╯┃╭╮┫╭╮┃╭╮╋┫╰╯┃┃┃┃┃┃┃━┫━━┫━━┫┃━┫╭╮┫╭╮┃┃━┫╭╯
┃╭━╮┃┃┃┃╰╯┃┃┃┃┃┃┃┃┃┃┃┃┃┃━╋━━┣━━┃┃━┫┃┃┃╰╯┃┃━┫┃
╰╯╱╰┻╯╰┻━━┻╯╰┻┻┻┻┻╯╰╯╰┻━━┻━━┻━━┻━━┻╯╰┻━╮┣━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯''')
	client = Client('192.168.56.1', 2007)
	client.connect(input('Enter the username --> '))