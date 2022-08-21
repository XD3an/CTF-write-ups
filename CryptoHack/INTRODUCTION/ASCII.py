from os import lseek
from traceback import format_tb


flag_enc = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for i in range(len(flag_enc)):
    print(chr(flag_enc[i]), end="")    