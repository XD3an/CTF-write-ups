flag_enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"


for i in range(len(flag_enc)):
    print(chr(ord(flag_enc[i])>>8), end="")
    print(chr((ord(flag_enc[i]))-((ord(flag_enc[i])>>8)<<8)), end="")
