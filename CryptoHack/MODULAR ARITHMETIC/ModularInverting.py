# Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a%b)
        return gcd, y, x - (a // b) * y

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
a, m = 3, 13
#inv = modinv(a, m)
inv = pow(a, -1, m) 
print(inv)