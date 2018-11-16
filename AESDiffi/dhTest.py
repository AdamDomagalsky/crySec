
from DiffieHellman import DiffieHellman

dhAlice = DiffieHellman()
g,p,publicKey = dhAlice.getBaseAndModulusAndPublicKey()
dhBob = DiffieHellman(g,p,publicKey)

print(dhBob.sharedSecret == dhAlice.calcSecret(dhBob.publicKey))
