from AESCipher import AESCipher
from random import randint
import sys
from Crypto.Util import number
import socket

obj = AESCipher('123234324234542dsfsdzdsdcsdcsdasd')

enc = obj.encrypt('siema')
print(enc)
dec = obj.decrypt(enc)
print(dec)


# teraz to wrzucamy do 3des
# https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

INIT_PRIME_SIZE = 10 # secound prime number will be twice +1 bigger

def getPrimeRoot():
  while True:
    q = number.getPrime(INIT_PRIME_SIZE)
    p = 2*q+1
    if number.isPrime(p):
      break

  while True:
    g = randint(2,p-1)
    if (pow(g,2,p) != 1) and (pow(g,q,p) != 1):
      return g, p

g, p = getPrimeRoot()


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 9999)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

  # Send data
  alicePrivateKey = randint(1,p-1)
  alicePublicKey  = pow(g,alicePrivateKey,p)
  message = str(g)+':'+str(p)+':'+str(alicePublicKey)


  print(sys.stderr, 'sending "%s"' % message)
  sock.sendall(message.encode('utf-8'))

  # Look for the response
  amount_received = 0
  amount_expected = len(message)

  while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print(sys.stderr, 'received "%s"' % data)
    bobPublicKey = data.decode('utf-8')
    bobPublicKey = int(bobPublicKey)
    alice = pow(bobPublicKey,alicePrivateKey,p)

    print('Alice key(%d): %d' % (alice.bit_length(), alice))


finally:
  print(sys.stderr, 'closing socket')
  sock.close()

