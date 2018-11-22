from AESCipher import AESCipher
from DiffieHellman import DiffieHellman

from random import randint
import sys
from Crypto.Util import number
import socket

aesOBJ = object()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9999)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

  # Send data
  dhAlice = DiffieHellman()
  g,p,alicePublicKey = dhAlice.getBaseAndModulusAndPublicKey()
  message = "DH|" + str(g)+':'+str(p)+':'+str(alicePublicKey)
  aliceSharedSecret = ""
  print('sending: %s' % message)
  sock.sendall(message.encode('utf-8'))

  while True:
    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
      data = sock.recv(500)
      amount_received += len(data)
      print('received: %s' % data.decode('utf-8'))
      header, body = data.decode('utf-8').split('|')

      if header == "DH":
        bobPublicKey = int(body)
        aliceSharedSecret = dhAlice.calcSecret(bobPublicKey)
        print('Alice SharedSecret(%d): %d' % (aliceSharedSecret.bit_length(), aliceSharedSecret))

        aesOBJ = AESCipher(str(aliceSharedSecret))
        enc = aesOBJ.encrypt('this is test AES cipher message')
        message = "AES|".encode('utf-8') + enc
        sock.sendall(message)

      elif header == "AES":
        decryptedBody = aesOBJ.decrypt(body)
        print("RESPONSE: %s" %decryptedBody)
        inpt = input('Your message > ')
        enc = aesOBJ.encrypt(inpt)
        message = "AES|".encode('utf-8') + enc
        sock.sendall(message)
      else:
        message = "UNKNOWN"
        sock.sendall(message.encode('utf-8'))

finally:
  print('closing socket')
  sock.close()

