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
    if (pow(g,2) != 1%p) and (pow(g,q,p) != 1%p):
      return g, p

g, p = getPrimeRoot()
alicePrivateKey = randint(1,p-1)
bobPrivateKey   = randint(1,p-1)
print('Alice private key: %d' % alicePrivateKey)
print('  Bob private key: %d' % bobPrivateKey)

alicePublicKey  = pow(g,alicePrivateKey,p)
bobPublicKey    = pow(g,bobPrivateKey,p)
print(' Alice public key: %d' % alicePublicKey)
print('   Bob public key: %d' % bobPublicKey)


alice = pow(bobPublicKey,alicePrivateKey,p)
bob = pow(alicePublicKey,bobPrivateKey,p)
print('        Alice key: %d' % alice)
print('          Bob key: %d' % bob)
print(' Same secret?\n\tA==B: %s' % (alice == bob))