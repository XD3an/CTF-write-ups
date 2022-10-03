def exgcd(a, b):
    # ax + by = gcd(a, b) 
		# Bézout's identity
    if(b == 0):
        return 1, 0, a
    else:
        x, y, q = exgcd(b, a%b)
        x, y = y, (x - (a // b) * y)
        return x, y, q

if __name__=='__main__':
    a, b = input().split(',')
    x, y, gcd = exgcd(int(a), int(b))
    print('x =', x, 'y =', y, 'gcd(', a ,',', b, ') =',  gcd)