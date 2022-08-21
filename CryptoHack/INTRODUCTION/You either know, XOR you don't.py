from pwn import *

flag_enc = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(flag_enc)

# find key (partial key)

# assume key = 'crypto{'
key = 'crypto{'

# Try ro find the key 
key = ''.join((chr(flag_enc[i] ^ ord(key[i]))) for i in range(7))
key += "y"    # add 'y'
key = key.encode()
print(key)

# extention the key
key = key * int((len(flag_enc)) / len(key))
key += key[:int((len(flag_enc)) % len(key))]
print(key)

# xor decode
flag = xor(flag_enc, key)

print(flag)
