import string
msg = [91, 322, 57, 124, 40, 406, 272, 147, 239, 285, 353, 272, 77, 110, 296, 262, 299, 323, 255, 337, 150, 102]

# string ascii lowercase
case = string.ascii_lowercase
case += string.digits
case += "_"

# flag initial
flag = "picoCTF{"

# decrypto
for i in range(len(msg)):
    flag+=case[msg[i]%37]
flag +="}"
# print
print(flag)