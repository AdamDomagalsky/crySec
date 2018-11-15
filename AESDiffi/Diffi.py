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
