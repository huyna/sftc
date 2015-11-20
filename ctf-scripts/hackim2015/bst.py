__author__ = 'HuyNA'
class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print chr(root.data),
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return
    print chr(root.data),
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

def post_order_print(root):
    if not root:
        return
    post_order_print(root.l_child)
    post_order_print(root.r_child)
    print chr(root.data),

a='sxbzuiS{ylfa490'

r = Node(ord('s'))
for i in xrange(len(a)-1):
    print a[i+1]
    binary_insert(r, Node(ord(a[i+1])))

print "in order:"
in_order_print(r)
print '\n'
print "pre order"
pre_order_print(r)
print '\n'
print "post order"
post_order_print(r)