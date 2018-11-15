from AESCipher import AESCipher
from random import randint
from Crypto.Util import number

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
  # Wait for a connection
  print(sys.stderr, 'waiting for a connection')
  connection, client_address = sock.accept()

  try:
    print(sys.stderr, 'connection from', client_address)

    # Receive the data in small chunks and retransmit it
    while True:
      data = connection.recv(16)
      print(sys.stderr, 'received "%s"' % data)
      if data:
        print(sys.stderr, 'sending data back to the client')

        g,p, alicePublicKey = data.decode('utf-8').split(':')
        g = int(g)
        p = int(p)
        alicePublicKey = int(alicePublicKey)
        print(g)
        print(p)
        print(alicePublicKey)
        bobPrivateKey = randint(1,p-1)
        bobPublicKey = pow(g,bobPrivateKey,p)
        message = str(bobPublicKey)

        bob = pow(alicePublicKey,bobPrivateKey,p)

        print('Bob key(%d): %d' % (bob.bit_length(), bob))



        print(sys.stderr, message.encode('utf-8'))
        connection.sendall(message.encode('utf-8'))
      else:
        print(sys.stderr, 'no more data from', client_address)
        break

  finally:
    # Clean up the connection
    connection.close()


