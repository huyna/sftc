__author__ = 'HuyNA'
"""
__nightmares__
Pwnables (375 pts)
The Plague is building an army of evil hackers, and they are starting off by teaching them python with this simple service.
Maybe if you could get full access to this system, at 54.196.37.47:9990, you would be able to find out more about The Plague's evil plans.


"""

#!/usr/bin/python -u
'''
You may wish to refer to solutions to the pCTF 2013 "pyjail" problem if
you choose to attempt this problem, BUT IT WON'T HELP HAHAHA.
'''

from imp import acquire_lock
from threading import Thread
from sys import modules, stdin, stdout

# No more importing!
x = Thread(target = acquire_lock, args = ())
x.start()
x.join()
del x
del acquire_lock
del Thread

# No more modules!

for k, v in modules.iteritems():
	if v == None: continue
	if k == '__main__': continue
	v.__dict__.clear()

del k, v

print modules

__main__ = modules['__main__']
modules.clear()
del modules

# No more anything!
del __builtins__, __doc__, __file__, __name__, __package__


#a = (12).__class__.__base__.__subclasses__()

print >> stdout, (12).__class__.__base__.__subclasses__()

print >> stdout, type[(12).__class__.__base__.__subclasses__()]

print >> stdout, "Get a shell. The flag is NOT in ./key, ./flag, etc."

while 1:
	exec 'print >> stdout, ' + stdin.readline() in {'stdout':stdout}