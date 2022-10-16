#! /usr/bin/python

from pwn import *

# ssh 
s = ssh(user='random', host='pwnable.kr', port=2222, password='guest')

# find key = 0xdeadbeef ^ random_number
# not real random...XD because no srand(seed)
random_number = 0x6b8b4567
key = 0xdeadbeef^random_number
success('key = %s', key)

# process
p = s.process(executable='./random')
p.sendline(str(key))
print(f'{p.recv()}\n{p.recv()}')

