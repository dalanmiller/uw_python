"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""


import select
import socket
import sys
import time
import datetime


host = 'localhost' 
port = 50000 
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


s.connect((host,port))

print 'echo_client connected to %s, on port %s, to exit type return ' %(host,port)

timeout = 30 # seconds
input = [s, sys.stdin]
running = True
while running:
    inputready,outputready,exceptready = select.select(input,[],[],timeout)

    # timeout
    if not inputready:  
        print 'Still alive at: %s' % (datetime.datetime.now())

    for x in inputready:

        if x == sys.stdin:
        	msg = sys.stdin.readline()
        	if msg == 'quit':
        		break
        	else:
	            # handle standard input
	            #msg = sys.stdin.readline()
	            #running = False
	            s.send('%s:%s' % (socket.gethostname(),msg))

        elif x: # client socket
            data = x.recv(size)
            print '%s' % (data.strip('\n'))
            if not data:
                x.close()
                

s.close()


