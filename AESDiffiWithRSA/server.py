from random import randint
from Crypto.Util import number

import socket
import sys
import pickle

from AESCipher import AESCipher
from DiffieHellman import DiffieHellman
from RSAdigitalSignature import verifyMsg

aesOBJ = object()


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 9998)
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
      data = connection.recv(4096)
      if data:
        data = pickle.loads(data)
        header = data['header']
        body = data['data']
        toSend = {}
        print('received: %s' % data)

        if header == "DH":
          if(verifyMsg(body['publicKey'], body['hasz'],body['signature'])):
            print('>>> DIGITAL SIGNATURE VERIFIED! <<<')

            g,p, alicePublicKey = body['message'].split(':')
            g = int(g)
            p = int(p)
            alicePublicKey = int(alicePublicKey)

            dhBob = DiffieHellman(g,p,alicePublicKey)
            toSend['header'] = 'DH'
            toSend['data'] = str(dhBob.publicKey)
            print('Bob SharedSecret(%d): %d' % (dhBob.sharedSecret.bit_length(), dhBob.sharedSecret))
            aesOBJ = AESCipher(str(dhBob.sharedSecret))
          else:
            print('DIGITAL SIGNATURE NOT VERIFIED!')
        elif header == "AES":
          decryptedBody =  aesOBJ.decrypt(body)
          print("RESPONSE: %s" % decryptedBody)
          inpt = input('Your message > ')
          enc = aesOBJ.encrypt(inpt)
          toSend['header'] = 'AES'
          toSend['data'] = enc

        else:
          toSend['header'] = ''
          toSend['data'] = ''
          break

        connection.sendall(pickle.dumps(toSend))
      else:
        print('no more data from', client_address)
        break

  finally:
    # Clean up the connection
    connection.close()


