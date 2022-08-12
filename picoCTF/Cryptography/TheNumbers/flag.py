import string

flag_enc = [16, 9, 3, 15, 3, 20, 6,'{', 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, '}']

case = string.ascii_uppercase

flag = ""
# print(flag_enc)

for i in range(len(flag_enc)):
    if flag_enc[i] == '{' or flag_enc[i] == '}':
        flag += flag_enc[i]
    else:
        flag += case[flag_enc[i]-1]
print(flag)