__author__ = 'HuyNA'
"RDDRRRRRRRRRRRRRRRRRRDDDDDDDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRUUUUUULLLLLLLLLDDRRRRRRDDLLLLLLLLLLLLLUURRRUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRUUUUUUUUUUUUULLLLLLLUUUURRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUURRRRRRRRRRRRRRRRRRRRRDRRRRRRRRRRRRRRUUULLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDRRRRRUUURRRRDDDDDLLLLLLLLLDDDDRRRRRRRRRRUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
"""
**########################################################################################
#*######################*******************************************#####*************#####
#************************####*####################################*#####*###########*#####
#########*#########*#########*#######***************************##*#####*###########*#####
#******##*#########*#########*#######*#########################*##*#####*###########*#####
#*####*##*#########*#########*#######*#########################*##*#####********####*#####
#*####*##*#########*######*******####*###**********####****####*##*############*####*#####
#*##***#**#########*#################*###*########*####*#######*##*############*####*#####
#*##*###*##########*##############****###*******##*####*#######*##*##*****#####*####*#####
#*##*###*##########*##############*############*##*####*#######*##*##*###*#####*####*#####
#************######*##############**************##*####*#######*##*##*###*#####*####*#####
###################*##############################*####***#####*##*##*###*#####*####*#####
###################********************************############*##*##*###*#####*####*#####
###############################################################*##*##*###*#####*####*#####
###***************************************************#########*##*##*###*#####*####*#####
###*#################################################*#########*##*######*#####*####*#####
###*####*****#####**********************#############*#########*##********#####*####*#####
###*####*###*#####*####################***************#########*###############*####*#####
###*####*###*#####*############################################*****************####*#####
###******###*#####*#################################################################*#####
############*#####*******************************************************************#####
###**********#############################################################################
###*#########*****************************************************************############
###*#########*###############################################*############################
###*#########*###############################################*######*****************#####
###**************************************************########*######*#####################
#############################################################*######*#####################
#############################################################*######*#####################
#########################*****************************************************************
"""

# re400
"""
    typedef struct _EXCEPTION_POINTERS
    {
        PEXCEPTION_RECORD ExceptionRecord;
        PCONTEXT          ContextRecord;
    } EXCEPTION_POINTERS, *PEXCEPTION_POINTERS;

    typedef struct _CONTEXT {
        //
        // The flags values within this flag control the contents of
        // a CONTEXT record.
        //
        // If the context record is used as an input parameter, then
        // for each portion of the context record controlled by a flag
        // whose value is set, it is assumed that that portion of the
        // context record contains valid context. If the context record
        // is being used to modify a threads context, then only that
        // portion of the threads context will be modified.
        //
        // If the context record is used as an IN OUT parameter to capture
        // the context of a thread, then only those portions of the thread's
        // context corresponding to set flags will be returned.
        //
        // The context record is never used as an OUT only parameter.
        //

        DWORD ContextFlags;

        //
        // This section is specified/returned if CONTEXT_DEBUG_REGISTERS is
        // set in ContextFlags. Note that CONTEXT_DEBUG_REGISTERS is NOT
        // included in CONTEXT_FULL.
        //

        DWORD Dr0;
        DWORD Dr1;
        DWORD Dr2;
        DWORD Dr3;
        DWORD Dr6;
        DWORD Dr7;

        //
        // This section is specified/returned if the
        // ContextFlags word contians the flag CONTEXT_FLOATING_POINT.
        //

        FLOATING_SAVE_AREA FloatSave;   // 112

        //
        // This section is specified/returned if the
        // ContextFlags word contians the flag CONTEXT_SEGMENTS.
        //

        DWORD SegGs;
        DWORD SegFs;
        DWORD SegEs;
        DWORD SegDs;

        //
        // This section is specified/returned if the
        // ContextFlags word contians the flag CONTEXT_INTEGER.
        //

        DWORD Edi;  // +156
        DWORD Esi;  // +160
        DWORD Ebx;  // +164
        DWORD Edx;  // +168
        DWORD Ecx;  // +172
        DWORD Eax;  // +176

        //
        // This section is specified/returned if the
        // ContextFlags word contians the flag CONTEXT_CONTROL.
        //

        DWORD Ebp;  // +180
        DWORD Eip;  // +184
        DWORD SegCs; // MUST BE SANITIZED
        DWORD EFlags; // MUST BE SANITIZED
        DWORD Esp;
        DWORD SegSs;

        //
        // This section is specified/returned if the ContextFlags word
        // contains the flag CONTEXT_EXTENDED_REGISTERS.
        // The format and contexts are processor specific
        //

        BYTE ExtendedRegisters[MAXIMUM_SUPPORTED_EXTENSION];

    } CONTEXT;


    typedef struct _FLOATING_SAVE_AREA
    {
        ULONG ControlWord;
        ULONG StatusWord;
        ULONG TagWord;
         ULONG ErrorOffset;
         ULONG ErrorSelector;
        ULONG DataOffset;
        ULONG DataSelector;
        UCHAR RegisterArea[80];
        ULONG Cr0NpxState;
    } FLOATING_SAVE_AREA, *PFLOATING_SAVE_AREA; // size = 112
"""
# re500

#joy300
"""
it_was_not_hard_rrly

01AFAF64  6E 72 54 72 6A 76 59 6D 60 7B 5C 7B 6D 5A 65 62  nrTrjvYm`{\{mZeb
01AFAF74  7B 6F 55 7A 71 62 77                             {oUzqbw

01AF9DCC  5F 43 65 43 5B 47 68 5C 51 4A 6D 4A 5C 6B 54 53  _CeC[Gh\QJmJ\kTS
01AF9DDC  4A 5E 64 4B 40 53 46 00                          J^dK@SF.

cipher
FF FF FF FF 17 00 00 00  5F 40 60 4A 58 42 6C 5C      ...._@`JXBl\
5B 4D 69 41 5B 65 51 56  43 5A 66 4D 4F 5C 42 00  [MiA[eQVCZfMO\B.
"""

cipher_text = "\x5F\x40\x60\x4A\x58\x42\x6C\x5C\x5B\x4D\x69\x41\x5B\x65\x51\x56\x43\x5A\x66\x4D\x4F\x5C\x42\x00"
size = len(cipher_text)

# re200
a1 = 1
a2 = 2

for i in xrange(87):
    temp = a1
    a1 = a2
    a2 += temp

print a1
print a2

"""
    4660046610375530309
    7540113804746346429

2880067194370816120
4660046610375530309
28800671943708161204660046610375530309

"""