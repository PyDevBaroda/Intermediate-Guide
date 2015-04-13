#importing a socket module
import socket
a = raw_input('Enter message to send: ')
#create a socket object
s = socket.socket()
# Get local machine name
host = socket.gethostname() 
# Open a port.
port = 12313 
#bind to port             
s.bind((host, port))
# wait for client to connect.
s.listen(5)
# Establish connection with client.
while True:
   c, addr = s.accept()
   print 'Got connection from', addr
   c.send(a)
   c.close()
   break;	      
