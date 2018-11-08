from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import polyval
from Crypto.Util import number
from random import randint


# Init section
secret = 12332
n = 10 # sharing parts 
k = 5 # minumum subsets to get secret back
primeNumber = number.getPrime(1000)

# Poly Factors
# factors = [secret,166, 94] # fX
factors = [secret]
for i in range(1,k):
  factors.append(randint(0,primeNumber))


# print(factors)

X = range(1, n+1) # x based on how many sharing parts
Dx1 = []
for i in X:
  Dx1.append(polyval(i,factors))
print(Dx1)
print(X)
print(primeNumber)

def _extended_gcd(a, b):
    x = 0
    last_x = 1
    y = 1
    last_y = 0
    while b != 0:
        quot = a // b
        a, b = b,  a%b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y
# print(_extended_gcd(31,4284))

def _divmod(num, den, p):

    inv, _ = _extended_gcd(den, p)
    return num * inv
def _lagrange_interpolate(x, x_s, y_s, p):

    k = len(x_s)
    assert k == len(set(x_s)), "points must be distinct"
    def PI(vals):  # upper-case PI -- product of inputs
        accum = 1
        for v in vals:
            accum *= v
        return accum
    nums = []  # avoid inexact division
    dens = []
    for i in range(k):
        others = list(x_s)
        cur = others.pop(i)
        nums.append(PI(x - o for o in others))
        dens.append(PI(cur - o for o in others))
    den = PI(dens)
    num = sum([_divmod(nums[i] * den * y_s[i] % p, dens[i], p)
               for i in range(k)])
    return (_divmod(num, den, p) + p) % p


secretBack = lagrange(X, Dx1)[0]
print(len(X))
print(_lagrange_interpolate(0, X[:-10], Dx1, primeNumber))
# print(secretBack)
