__author__ = 'HuyNA'

"""
    input:
        la 1 chuoi co kich thuoc < 250
        tap hop cac ki tu: X, Y, Z, Q, (),
"""

#for i in range(256):
#    print "python -c 'a=0x"+chr(i).encode("hex")+";print chr(a)+\"\\n\"' | ./weird_snus \"(XXXXXXX\""
    #print "\n"

a=0x00;mess=chr(a)+"\n";mess+="a"*249+"\n";print mess
a=0x00;mess=chr(a)+"\n";mess+="a"*249+"\n"+"D\n"+"../\n"+"C\n"+"A\n"+"G\xFF\n";print mess