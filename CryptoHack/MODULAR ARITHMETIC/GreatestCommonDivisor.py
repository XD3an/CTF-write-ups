

def gcd(a, b):
    # print("New *a* is " + str(a) + ", new *b* is " + str(b))
    if b == 0:
        # print("b is 0, stopping recursion, a is the gcd: " + str(a))
        return a
    # print("Recursing with new a = b and new b = a % b...")
    return gcd(b, a % b)


print(gcd(66528,52920))