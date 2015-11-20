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

__main__ = modules['__main__']
modules.clear()
del modules

# No more anything!
del __builtins__, __doc__, __file__, __name__, __package__

_type = (12).__class__.__base__.__subclasses__()[0];
_list = (12).__class__.__base__.__subclasses__()[7];
_set = (12).__class__.__base__.__subclasses__()[14];

#print >> stdout, (12).__class__.__base__.__subclasses__()[2];

#print >> stdout, (12).__class__.__base__.__subclasses__()[54];

#print >> stdout, (12).__class__.__base__.__subclasses__()[i]()._module;
#print >> stdout, (12).__class__.__base__.__subclasses__()[i].__dict__['__module__'];
#print >> stdout, (12).__class__.__base__.__subclasses__()[i].__module__;


# b = classes[49]()._module.__builtins__
# func_globals =>
# __dict__ =>
i = 61;
a = (12).__class__.__base__.__subclasses__()[i];
#print >> stdout, a.__call__.func_globals

print >> stdout, "\naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# __main__ => <type 'module'>
print >> stdout, a.__dict__
print >> stdout, a

print >> stdout, a.__doc__


print >> stdout, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

print >> stdout, "\n"
# type 'getset_descriptor' =>
"""
# _type(a.__dict__['_note']) => <type 'function'>
        func_globals


"""
print >> stdout, "GET A SHELL. THE FLAG IS NOT IN ./KEY, ./FLAG, ETC."
#while 1:
#	exec 'print >> stdout, ' + stdin.readline() in {'stdout':stdout}

"""
 <class 'warnings.WarningMessage'>
 <class 'warnings.catch_warnings'>
 <class '_weakrefset._IterationGuard'>
 <class '_weakrefset.WeakSet'>
 <class '_abcoll.Hashable'>
 <class '_abcoll.Iterable'>
 <class '_abcoll.Sized'>
 <class '_abcoll.Container'>
 <class '_abcoll.Callable'>
 <class 'site._Printer'>
 <class 'site._Helper'>
 <class 'site.Quitter'>
 <class 'codecs.IncrementalEncoder'>
 <class 'codecs.IncrementalDecoder'>
 <class 'threading._Verbose'>
"""