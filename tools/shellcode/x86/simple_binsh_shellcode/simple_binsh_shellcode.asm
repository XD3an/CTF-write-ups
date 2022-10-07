section .text
global _start
_start:
    xor ecx, ecx
    xor edx, edx
    
    ; kint execve("/bin/sh", 0, 0)
    xor eax, eax
    mov eax, 0x0b
    push "/sh"     ; "hs/"
    push "/bin"    ; "nib/"
    mov ebx, esp
    mov ebx, esp
    int 0x80
