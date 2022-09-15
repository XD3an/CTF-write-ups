#! /usr/bin/python

from pwn import *

# ssh
s = ssh(user='col', host='pwnable.kr', port=2222, password='guest')

# payload
"""
hex(0x21DD09EB/5)
'0x6c5cec7'

hex(0x6c5cec7*4)
'0x1b173b1f'

hex(0x6c5cec7*5)
'0x21dd09e7'

hex(0x21dd09eb-0x6c5cec8*4)
'0x6c5cecb'
"""
payload = b'\xc8\xce\xc5\x06'*4+ b'\xcc\xce\xc5\x06'
#payload = p32(0x6c5cec8) * 4 + p32(0x6c5cecc)

p = s.process(executable='./col', argv=['col',payload])

print(p.recv())


