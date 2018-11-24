from random import randint
from Crypto.Util import number

import socket
import sys
import pickle

from AESCipher import AESCipher
from DiffieHellman import DiffieHellman
from RSAdigitalSignature import signMsg

aesOBJ = object()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9998)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

  # Diffie Hellman
  dhAlice = DiffieHellman()
  aliceSharedSecret = ''
  g,p,alicePublicKey = dhAlice.getBaseAndModulusAndPublicKey()
  message = str(g)+':'+str(p)+':'+str(alicePublicKey)

  # Send data
  toSend =  {}
  toSend['header'] = 'DH'
  toSend['data'] = signMsg(message)
  print('sending: %s' % toSend)
  sock.sendall(pickle.dumps(toSend))

  while True:
    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
      data = sock.recv(4096)
      amount_received += len(data)
      # print('received: %s' % data.decode('utf-8'))
      # header, body = data.decode('utf-8').split('|')
      data = pickle.loads(data)
      header = data['header']
      body = data['data']

      if header == "DH":
        bobPublicKey = int(body)
        aliceSharedSecret = dhAlice.calcSecret(bobPublicKey)
        print('Alice SharedSecret(%d): %d' % (aliceSharedSecret.bit_length(), aliceSharedSecret))

        aesOBJ = AESCipher(str(aliceSharedSecret))
        enc = aesOBJ.encrypt('this is test AES cipher message')
        toSend['header'] = 'AES'
        toSend['data'] = enc
      elif header == "AES":
        decryptedBody = aesOBJ.decrypt(body)
        print("RESPONSE: %s" %decryptedBody)
        inpt = input('Your message > ')
        enc = aesOBJ.encrypt(inpt)

        toSend['header'] = 'AES'
        toSend['data'] = enc
      else:
        toSend['header'] = ''
        toSend['data'] = "UNKNOWN"
      sock.sendall(pickle.dumps(toSend))

finally:
  print('closing socket')
  sock.close()

