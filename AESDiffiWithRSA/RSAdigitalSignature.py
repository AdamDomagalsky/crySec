import base64
import pickle
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random


def signMsg(messageToBeSigned):
  random_generator = Random.new().read
  RSAkey = RSA.generate(1024, random_generator) #generate public and private keys
  hasz = SHA256.new(messageToBeSigned.encode('utf-8')).digest()
  signature = RSAkey.sign(hasz, random_generator)
  publicKey = RSAkey.publickey().exportKey('PEM')
  return {'publicKey':publicKey, 'hasz':hasz, 'signature':signature, 'message':messageToBeSigned}


def verifyMsg(publicKey, hasz, signature):
  return RSA.importKey(publicKey).verify(hasz,signature)
