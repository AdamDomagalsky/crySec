from Crypto.Util import number
from random import randint
from numpy.polynomial.polynomial import polyval
from scipy.interpolate import lagrange

primeNumber = number.getPrime(256)

# t <= n
n = 10 # ilosc generalow
t = 5 #ilu potrzeba zeby odtworzyc skeret
Secret = 999 # a0 w wielomianie
factors = [Secret]
shares = [] # czesci sekretow


for i in range(1, t):
  factors.append(randint(0,primeNumber))
print(len(factors))

for i in range(1, n+1):
  shares.append(polyval(i,factors) % primeNumber)

print(len(shares))

chosensIndex = []
chosens = []
for i in range(0, t):
  element = randint(0,len(shares)-1)
  chosensIndex.append(element)
  chosens.append(shares[element])
  del shares[element]



print(lagrange(chosens,chosensIndex))