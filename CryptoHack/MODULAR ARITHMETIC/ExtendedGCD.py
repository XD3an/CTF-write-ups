
# Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a%b)
        return gcd, y, x - (a // b) * y

a, b = 11, 6
g, x, y = extended_gcd(a, b)
print("gcd(", a , "," , b, ") = ", g, "x = ", x, "y = ", y)