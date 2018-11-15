from random import randint
import sys
from Crypto.Util import number
# teraz to wrzucamy do 3des
# https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

INIT_PRIME_SIZE = 512 # secound prime number will be twice +1 bigger

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
alicePrivateKey = randint(1,p-1)
bobPrivateKey   = randint(1,p-1)
print('Alice private key(%d): %d' % (alicePrivateKey.bit_length(), alicePrivateKey))
print('  Bob private key(%d): %d' % (bobPrivateKey.bit_length(), bobPrivateKey))

alicePublicKey  = pow(g,alicePrivateKey,p)
bobPublicKey    = pow(g,bobPrivateKey,p)
print(' Alice public key(%d): %d' % (alicePublicKey.bit_length(), alicePublicKey))
print('   Bob public key(%d): %d' % (bobPublicKey.bit_length(), bobPublicKey))


alice = pow(bobPublicKey,alicePrivateKey,p)
bob = pow(alicePublicKey,bobPrivateKey,p)
print('        Alice key(%d): %d' % (alice.bit_length(), alice))
print('          Bob key(%d): %d' % (bob.bit_length(), bob))
print(' Same secret?\n\tA==B: %s' % (alice == bob))