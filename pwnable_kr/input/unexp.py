#! /usr/bin/python

from pwn import *
import os

s = ssh(user='input2', host='pwnable.kr', port=2222, password='guest')

# argv
argv=list(' '*100)
argv[0] = './input'
argv[ord('A')] = "\x00"
argv[ord('B')] = "\x20\x0a\x0d"
#print(argv[ord('A')], argv[ord('B')])

# stdio
r_stdin, w_stdin = os.pipe()
r_stderr, w_stderr = os.pipe()

os.write(w_stdin, b"\x00\x0a\x00\xff")
os.write(w_stderr, b"\x00\x0a\x02\xff")

# process
p = s.process(executable='./input', argv=argv, stdin=r_stdin, stderr=r_stderr)
# garbage
print(p.recv())
print(p.recv())
print(p.recv())
# Stage 1 clear!
print(p.recv())
# Stage 2 clear!
print(p.recv())
print(p.recv())
