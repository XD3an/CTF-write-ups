# Introduction

This crackme is another easy one, but different than most I have added so far. It is a simple CD-Rom check. If the Crackme thinks your hard drive is a CD-Rom it displays a message saying "OK, I really think that your HD is a CD-ROM! :p " or else it says "NAH... This is not a CD-ROM drive!"
The only thing to do with this one is patch it, so what the hell are we waiting for?!

# Solution


I using x32 dbg to dynamic analysis the program, and we can use string table to find the string "OK, I really think that your HD is a CD-ROM! :p", and we can see the string "Error,...." before this string.

### method1 : Change instruction

We can see the instruction "je abexcm1,40103D" before them two strings.
Although we don't know what is abexcm1.40103D, but we can know there is a jump instruction, and before the instruction have a cmp instruction.
In summary, we can know the program is judge something then according to the result to output something in the MessageBox. 

```
00401024 | 3BC6                     | cmp eax,esi                             | esi:EntryPoint
00401026 | 74 15                    | je abexcm1.40103D                       | 
00401028 | 6A 00                    | push 0                                  |
0040102A | 68 35204000              | push abexcm1.402035                     | 402035:"Error"
0040102F | 68 3B204000              | push abexcm1.40203B                     | 40203B:"Nah... This is not a CD-ROM Drive!"
00401034 | 6A 00                    | push 0                                  |
00401036 | E8 26000000              | call <JMP.&MessageBoxA>                 |
0040103B | EB 13                    | jmp abexcm1.401050                      |
0040103D | 6A 00                    | push 0                                  |
0040103F | 68 5E204000              | push abexcm1.40205E                     | 40205E:"YEAH!"
00401044 | 68 64204000              | push abexcm1.402064                     | 402064:"Ok, I really think that your HD is a CD-ROM! :p"
00401049 | 6A 00                    | push 0                                  |
0040104B | E8 11000000              | call <JMP.&MessageBoxA>                 |
00401050 | E8 06000000              | call <JMP.&ExitProcess>                 |

```
According testing, we know the result of "cmp" is always false, so if we change "je" to "jne", we can pass the judgement.
* je abexcm1.40103D -> jne abexcm1.40103D

