import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5556)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

s="" #string buffer

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        s+= data
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

    print "Recieved from EchoServer: " + s
    sock.sendall("quit") #quits the server
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
