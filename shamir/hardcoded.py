from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import polyval



secret = 666
n = 6 # sharing parts
k = 3 # minumum subsets

fX = [secret, 166, 94, 54]
X = range(1,n+1)
Dx1 = []
for i in X:
  Dx1.append(polyval(i,fX))
print(Dx1)
secretBack = lagrange(X, Dx1)[0]

print(secretBack)
