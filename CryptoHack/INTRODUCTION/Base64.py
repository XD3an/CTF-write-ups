import base64

flag_enc = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# hex to bytes
flag_enc = bytes.fromhex(flag_enc)
print(flag_enc)

# bytes to base64
flag_enc = base64.b64encode(flag_enc)
print(flag_enc)
