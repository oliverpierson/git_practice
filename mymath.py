def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def binomial(n, k):
    return fact(n) / ( fact(k) * fact(n-k) )
