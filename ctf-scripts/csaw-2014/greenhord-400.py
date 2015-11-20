__author__ = 'HuyNA'
'''
nc 54.164.253.42 9998

This is one of those "key" challenges we talked about on the stream.
Also, you should just CreateFile and WriteFile to stdout for your shellcode.
Anything more complicated is probably blocked by the App Container.

Update: You can use AppJailLauncher to launch greenhornd.exe just like the game server does with:
AppJailLauncher.exe /network /key:key /port:9998 /timeout:30 greenhornd.exe

Written by RyanWithZombies

greenhornd.exe
AppJailLauncher.exe


.rdata:004030A0     aWecomeToTheGre db 'Wecome to the Greenhorn CSAW service!',0Ah
.rdata:004030A0                                             ; DATA XREF: _main+29o
.rdata:004030A0                     db 'This service is a Windows 8.1 Pwnable! You',27h,'re going to need a '
.rdata:004030A0                     db 'Windows 8.1 computer or VM to solve this one. If you don',27h,'t hav'
.rdata:004030A0                     db 'e a Windows Key, I suggest using Amazon EC2: http://aws.amazon.co'
.rdata:004030A0                     db 'm/windows/',0Ah
.rdata:004030A0                     db 0Ah
.rdata:004030A0                     db 'Windows Exploitation is new to a lot of you, so this is a tutoria'
.rdata:004030A0                     db 'l service! To start, let',27h,'s install some software you',27h,'ll nee'
.rdata:004030A0                     db 'd to follow along:',0Ah
.rdata:004030A0                     db 9,'Windows SDK for the debugging tools (http://msdn.microsoft.com/e'
.rdata:004030A0                     db 'n-us/windows/desktop/bg162891.aspx)',0Ah
.rdata:004030A0                     db 9,'MSYS for nice command line tools (http://www.mingw.org/wiki/MSYS'
.rdata:004030A0                     db ')',0Ah
.rdata:004030A0                     db 9,'IDA Free (https://www.hex-rays.com/products/ida/support/download'
.rdata:004030A0                     db '_freeware.shtml)',0Ah
.rdata:004030A0                     db 9,'NASM for Windows (http://www.nasm.us/pub/nasm/releasebuilds/2.11'
.rdata:004030A0                     db '.05/win32/)',0Ah
.rdata:004030A0                     db 0Ah
.rdata:004030A0                     db 'To continue, you',27h,'re going to need the password. You can get th'
.rdata:004030A0                     db 'e password by running strings from minsys (strings - greenhorn.ex'
.rdata:004030A0                     db 'e) or locate it in IDA.',0Ah
.rdata:004030A0                     db 0Ah
.rdata:004030A0                     db 'Password: ',0
.rdata:00403409                     align 4
.rdata:0040340C     ; char Str2[]

db 0Ah                  ; DATA XREF: sub_4013C0+3o
                db 0Ah
                db 'NX/DEP',0Ah
                db '------',0Ah
                db 0Ah
                db 'There are a few techniques to defeat NX/DEP on Windows! The most '
                db 'popular routes are to call VirtualProtect or VirtualAlloc with PA'
                db 'GE_EXECUTE_READWRITE set for fwProtect.',0Ah
                db 'The only issue iyou need to have a reference to the function in k'
                db 'ernel32 or have it convienently imported for you in something you'
                db ' have an ASLR leak to.',0Ah
                db 0Ah
                db 'This looks like a decent resource: http://blog.harmonysecurity.co'
                db 'm/2010/04/little-return-oriented-exploitation-on.html',0Ah
                db 0Ah
                db 'You can also do something ugly like call WriteProcessMemory().',0Ah
                db 0Ah,0
                align 4
aBye            db 'Bye!',0Ah,0         ; DATA XREF: a_print_bye_string+3o


.rdata:00402690     Format          db 'Static Analysis',0Ah ; DATA XREF: sub_4012C0+4Co
.rdata:00402690                     db '---------------',0Ah
.rdata:00402690                     db 'Fire up IDA Free (or Pro) and load in this binary! You can ignore'
.rdata:00402690                     db ' a lot of the setup functionas they deal with sandboxing this cha'
.rdata:00402690                     db 'llenge.',0Ah
.rdata:00402690                     db 0Ah
.rdata:00402690                     db 'The functions of interest start at %08x.',0Ah
.rdata:00402690                     db 'I',27h,'d start by checking all the stack variable sizes with alt+k!'
.rdata:00402690                     db 0Ah
.rdata:00402690                     db 0Ah,0

  wprintf(L"    /key:key-file-path  This switch specifies a file that should be used as\n");
  wprintf(L"                        the \"key\" file in a capture-the-flag challenge. By\n");
  wprintf(L"                        specifying a file, the file and the file's parent\n");
  wprintf(L"                        directory will both have new access control entries\n");
  wprintf(L"                        added to their access control lists allowing the current\n");
  wprintf(L"                        AppContainer read access.\n");
'''

