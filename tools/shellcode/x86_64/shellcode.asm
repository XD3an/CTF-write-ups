; execve("/bin/sh", ["/bin/sh"], NULL)
    
section .text
global _start
                     
_start:
    ; int execve("/bin/sh", 0, 0)
    xor     rdx, rdx
    mov     qword rbx, '//bin/sh'
    shr     rbx, 0x8
    push    rbx
    mov     rdi, rsp
    push    rax
    push    rdi
    mov     rsi, 0
    mov     al, 0x3b
    syscall
