# #Read a givin file
# import sys
# import os
# inp=""
# if (len(sys.argv)>1):# if filename is given
#     inp = sys.argv[1]#get filename
# if inp:#print it out
#     file = open(r"c:\classEx\someFile.txt","r+")
#     data = file.read()
#     print (data)
#     file.close()
# else:
#     print("usage:readfile filename")
#Echo Server

import socket
import sys
fn="c:\classEx\ex.txt"
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #makes a TCP block using address family INET

# Bind the socket to the port
server_address = ('localhost', 6667)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    s="" #string buffer
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:

            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                s += data #adds input to s
                if s.contains("GET /HTTP/1.1"):
                      file = open(fn,"r+")
                      data = file.read()
                      connection.sendall(data)
                if s == "quit": #resets s and breaks
                    break
                if data == ".":
                    connection.sendall(s+'\r\n') #Sends the sentence
                    s = ""
            else:
                print >>sys.stderr, 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        print("Peace")
        connection.sendall("\r\nGood bye" + '\r\n')
        connection.close()
        break

