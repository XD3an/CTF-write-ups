# Pwnable.kr - leg

# key

```arm
    0x00008d68 <+44>:	bl	0x8cd4 <key1>
    0x00008d6c <+48>:	mov	r4, r0
    0x00008d70 <+52>:	bl	0x8cf0 <key2>
    0x00008d74 <+56>:	mov	r3, r0
    0x00008d78 <+60>:	add	r4, r4, r3
    0x00008d7c <+64>:	bl	0x8d20 <key3>
    0x00008d80 <+68>:	mov	r3, r0
    0x00008d84 <+72>:	add	r2, r4, r3
    0x00008d88 <+76>:	ldr	r3, [r11, #-16]
    0x00008d8c <+80>:	cmp	r2, r3
```

* key1 = 0x00008ce0+4  
```arm
    0x00008cdc <+8>:	mov	r3, pc
    0x00008ce0 <+12>:	mov	r0, r3
```
* key2 = 0x00008d08+4  
```arm
    0x00008cfc <+12>:	add	r6, pc, #1
    0x00008d00 <+16>:	bx	r6
    0x00008d04 <+20>:	mov	r3, pc
    0x00008d06 <+22>:	adds    r3, #4
    0x00008d10 <+32>:	mov	r0, r3
```
* key3 = 0x00008d80    
```arm
    0x00008d28 <+8>:	mov	r3, lr
    0x00008d2c <+12>:	mov	r0, r3
```
* key = (0x00008ce0+4) + (0x00008d08+4) + (0x00008d80) = 108400

# Pwn

```
/ $ ./leg
Daddy has very strong arm! : 108400
Congratz!
My daddy has a lot of ARMv5te muscle!
```