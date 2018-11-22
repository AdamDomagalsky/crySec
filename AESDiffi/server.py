from AESCipher import AESCipher
from random import randint
from Crypto.Util import number
from DiffieHellman import DiffieHellman

aesOBJ = object()

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9999)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
  # Wait for a connection
  print('waiting for a connection')
  connection, client_address = sock.accept()

  try:
    print('connection from', client_address)
    # Receive the data in small chunks and retransmit it
    while True:
      data = connection.recv(500)
      if data:
        print('received: %s' %data.decode('utf-8'))

        header, body = data.decode('utf-8').split('|')

        if header == "DH":
          g,p, alicePublicKey = body.split(':')
          g = int(g)
          p = int(p)
          alicePublicKey = int(alicePublicKey)

          dhBob = DiffieHellman(g,p,alicePublicKey)
          message = "DH|" + str(dhBob.publicKey)
          message = message.encode('utf-8')
          # bobSharedSecret = pow(alicePublicKey,bobPrivateKey,p)
          print('Bob SharedSecret(%d): %d' % (dhBob.sharedSecret.bit_length(), dhBob.sharedSecret))
          aesOBJ = AESCipher(str(dhBob.sharedSecret))
        elif header == "AES":
          decryptedBody =  aesOBJ.decrypt(body)
          print("RESPONSE: %s" % decryptedBody)
          inpt = input('Your message > ')
          enc = aesOBJ.encrypt(inpt)
          message = "AES|".encode('utf-8') + enc

        else:
          message = "UNKNOWN"
          break

        connection.sendall(message)
      else:
        print('no more data from', client_address)
        break

  finally:
    # Clean up the connection
    connection.close()


