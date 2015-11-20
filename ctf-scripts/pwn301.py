__author__ = 'HuyNA'

"""
    Points: 301

We have developed a brand new "exploit mitigation" that makes it IMPOSSIBLE to reverse engineer our apps! File running
at fuzzy.2014.ghostintheshellcode.com 4141
"""

def decrypt_function(buffer):
    """

    """
    nop = "\x90\x90\x90\x90\x90\x90"
    count = 0
    ok = 0
    while 1:
        temp = ~buffer[count] & 0xFF
        buffer[count] = temp
        if count > 6:
            temp_count = count - 6
            temp_str = buffer[temp_count:count]
            if temp_str == nop:
                ok = 1
        else:
            if ok == 1:
                if buffer[count] == "\xC3":
                    break
        count += 1


