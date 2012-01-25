"""
echo client, usage:

 python echo_client.py <host> <port>

Both host and port are optional, defaults: localhost 50000
host must be present if you want to provide port
"""

import socket 
import sys
import select
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

print 'echo_client listening on port %s, to exit type return ' % port

timeout = 5 # seconds
input = [s, sys.stdin]
running = True
while running:
    inputready,outputready,exceptready = select.select(input,[],[],timeout)

    # timeout
    if not inputready:  
        print '%s' % (datetime.datetime.now())

    for s in inputready:

        elif s == sys.stdin:
            # handle standard input
            junk = sys.stdin.readline()
            running = False
            print 'Input %s from stdin, exiting.' % junk.strip('\n')

        elif s: # client socket
            data = s.recv(size)
            print '%s: %s' % (s.getpeername(), data.strip('\n'))
            if not data:
                s.close()
                print 'closed connection'
                input.remove(s)

s.close()


