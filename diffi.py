from random import randint
import sys
from Crypto.Util import number
# teraz to wrzucamy do 3des
# https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

INIT_PRIME_SIZE = 200 # secound prime number will be twice +1 bigger

def getPrimeRoot():
  while True:
    q = number.getPrime(INIT_PRIME_SIZE)
    p = 2*q+1
    if number.isPrime(p):
      break

  while True:
    g = randint(2,p-1)
    if (g**2 != 1%p) and (g**q != 1%p):
      return g, p


g, p = getPrimeRoot()

alicePrivateKey = randint(1,p-1)
bobPrivateKey   = randint(1,p-1)
print('Alice private key: %d' % alicePrivateKey)
print('Bob private key:   %d' % bobPrivateKey)

alicePublicKey  = (g**alicePrivateKey)  % p
bobPublicKey    = (g**bobPrivateKey)    % p
print('Alice public key:  %d' % alicePublicKey)
print('Bob public key:    %d' % bobPublicKey)


alice = (bobPublicKey**alicePrivateKey) % p
bob = (alicePublicKey**bobPrivateKey)   % p
print('Alice key: %d' % alice)
print('Bob key:   %d' % bob)

print(alice == bob)





