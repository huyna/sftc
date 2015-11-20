__author__ = 'HuyNA'

import sys

# globals
# d = 0x10001
d = 65537
n = 22560707967953561594777252966706754723085578687226105030079212475326639700463552018673641414819
# n = 2^3*11*59*43452827365087753456812890922008387371120143850589570551
m = 0x3004
# m =12292 = 2^2*7*439
def main():
    # args?
    if len(sys.argv) != 2:
        print "usage: ", sys.argv[0], "<serial>";
        quit()

    c = int(sys.argv[1], 10);

    # process, check
    if pow(c, d, n) == m:
        print "now submit that as your flag"
    else:
        print "do not even try"
print 0,"\t",n
for i in range(50,60):
    a = (i**d) % n
    print i,"\t",a

#print n**2