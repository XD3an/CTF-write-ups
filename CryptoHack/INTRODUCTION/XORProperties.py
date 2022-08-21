from pwn import *

flag_enc = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"

# hex to bytes
flag_enc = bytes.fromhex(flag_enc)
KEY1 = bytes.fromhex(KEY1)
KEY2_KEY1 = bytes.fromhex(KEY2_KEY1)
KEY2_KEY3 = bytes.fromhex(KEY2_KEY3)

# KEY2, KEY3
KEY2 = xor(KEY1, KEY2_KEY1)
print(KEY2)

KEY3 = xor(KEY2, KEY2_KEY3)
print(KEY3)


# decode 
print(xor(flag_enc, KEY1, KEY2, KEY3))
