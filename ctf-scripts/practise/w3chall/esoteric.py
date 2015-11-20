__author__ = 'HuyNA'

"""

ssh esoteric3@wargame.w3challs.com -p 20202

The password is in file /home/esoteric3/flag (readable only by user esoteric3_pwned).
ASLR and NX are enabled on this VM.

esoteric3@W3Hack ~ $ ls -l
total 2060
-r-------- 1 esoteric3_pwned esoteric3_pwned      34 Apr 28 21:52 flag
-r-sr-x--- 1 esoteric3_pwned esoteric3       2098747 May  1 13:12 tinypwn
esoteric3@W3Hack ~ $ ls -la
total 2068
dr-xr-x---  2 esoteric3       esoteric3          4096 Apr 28 21:03 .
drwxr-x--x 30 root            root               4096 Apr 28 21:00 ..
-r--------  1 esoteric3_pwned esoteric3_pwned      34 Apr 28 21:52 flag
-r-sr-x---  1 esoteric3_pwned esoteric3       2098747 May  1 13:12 tinypwn
esoteric3@W3Hack ~ $ id
uid=1028(esoteric3) gid=1030(esoteric3) groups=1030(esoteric3)
esoteric3@W3Hack ~ $


tai file


%rax	System call	        %rdi	                %rsi	                    %rdx	                    %rcx	%r8	%r9
59	    sys_execve	        const char *filename	const char *const argv[]	const char *const envp[]
"""