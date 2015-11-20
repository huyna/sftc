__author__ = 'HuyNA'

import immlib
import getopt
import immutils
from immutils import *

imm = immlib.Debugger()

"""
 Functions
"""
def write_to_log_window():
    global  imm
    imm.log("[+] Begin Log ")
    imm.log("Number of arguments : %d " % 12)

class ConditionBp(immlib.LogBpHook):

    def __init__(self):
        immlib.LogBpHook.__init__(self)

    def run(self, regs):
        global imm
        imm.log("==========================================================")
        # can print:
        #   eax => buffer to decode
        imm.log("   Buffer2Decode EAX = %08x" % regs['EAX'])
        Buffer2Decode = imm.readMemory(regs['EAX'], 24)
        imm.log(Buffer2Decode.encode("hex"))

        #   edx => buffer key
        imm.log("   BufferKey EDX = %08x" % regs['EDX'])
        BufferKey = imm.readMemory(regs['EDX'], 50)
        imm.log(BufferKey.encode("hex"))

        #   0045CE20 => count frame
        imm.log("   CountFrame [0045CE20] = %08x" % imm.readLong(0x0045CE20))

        #   0045CE18 => count bypass
        imm.log("   CountBypass [0045CE18] = %08x" % imm.readLong(0x0045CE18))

        return 1

"""
 Main application
"""
def main(args):
    global imm
    imm.log("[+] Begin Seting LogBpHook ")

    # dat break tai 004581B4 voi handler nhu ham co san
    newHook = ConditionBp()
    newHook.add("ConditionBP1", 0x004581B4)

    return "[+] Hook Installed"
