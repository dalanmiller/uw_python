"""
echo server, usage:

 python echo_server.py <port>

Port is optional, default: 50000
"""
import os
import socket 
import sys
import time

host = '' 
port = 50000 

if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'echo_server listening on port', port
s.listen(backlog) 

clients = []
while True: 
    client, address = s.accept()
    clients.append(client) 
    print "%s connected at %s" % (address, time.ctime())
    while True:
        data = client.recv(size)       
        if not data: break
        #for c in clients:
        #    c.send(b'Polo: %s' % data)
        #    print "%s to %s" % (data, 'IP') 
        print data
        
    clients.remove(client)
    client.close()
