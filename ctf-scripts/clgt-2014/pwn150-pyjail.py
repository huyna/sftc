"""
    pyjail 150
"""

from sys import modules
modules.clear()
del modules

__builtins__.dir = None
eval = None
input = None
execfile = None

F_L_A_G = '1111'#open('./flag','r').read()

I_N_P_U_T = (list(globals()[list(globals())[8]])) # only a-z0-9[]() and length of code must be <= 50

print I_N_P_U_T

if I_N_P_U_T == list(F_L_A_G):
	print I_N_P_U_T


a = ['e', 'z', '_', 'B', 'r', '3', '4', 'k']