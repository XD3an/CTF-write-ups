section .text
global _start

_start:
    ; int execve("/bin/sh", 0, 0)
    xor ecx,ecx
    mul ecx
    mov al, 11
    push ecx
    push 0x68732f2f    ; "/sh"
    push 0x6e69622f    ; "/bin"
    mov ebx, esp
    int 0x80
