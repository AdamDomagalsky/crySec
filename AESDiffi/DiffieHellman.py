from Crypto.Util import number

class DiffieHellman(object):
  """Diffie Hellman secret sharing

    __init__(g, p, publicKey):
      Give 3 args or none, if none were given,
      they will be generated (+private key and +shared secret)

    Attributes
      g (int): g is a primitive root modulo p.
      p (int): modulus, that p=2*q+1, where q is a Prime number
      __privateKey (int)
      publicKey (int)
      sharedSecret (int)

    """
  INIT_PRIME_SIZE: int = 128
  g: int = 5
  p: int = 23
  __privateKey: int = 0
  publicKey: int = 0
  sharedSecret: int = 0

  def __getNewPrimeRoot(self):
    """ Calculates prime roots

      Returns:
        g(int), p(int)

    """
    while True:
      q = number.getPrime(self.INIT_PRIME_SIZE)
      p = 2*q+1
      if number.isPrime(p):
        break

    while True:
      g = number.getRandomRange(2,p)
      if (pow(g,2,p) != 1) and (pow(g,q,p) != 1):
        return g, p

  def __init__(self, g = 0, p = 0, publicKey = 0):

    if g == 0 or p == 0:
      self.g, self.p = self.__getNewPrimeRoot()
      self.__privateKey = number.getRandomRange(2,self.p)
      self.publicKey = pow(self.g, self.__privateKey, self.p)
    else:
      self.g, self.p = g, p
      self.__privateKey = number.getRandomRange(2,self.p)
      self.publicKey = pow(self.g, self.__privateKey, self.p)
      self.sharedSecret = pow(publicKey,self.__privateKey,self.p)

  def getBaseAndModulusAndPublicKey(self):
    """
      Returns: g(int), p(int), publicKey(int)
    """
    return self.g, self.p, self.publicKey

  def calcSecret(self, publicKey):
    """ Calculates shared secret: pow(publicKey,self.__privateKey,self.p)

      Arg:
        publicKey(int): from Bob

      Returns:
        sharedSecret(int)
    """
    self.sharedSecret = pow(publicKey,self.__privateKey,self.p)
    return self.sharedSecret



