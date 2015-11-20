from sys import modules
modules.clear()
del modules

__builtins__.dir = None
eval = None
input = None
execfile = None

LEN_PASS = len(open('./password','r').read()) # Length of Password


# only a-z0-9[]() and length of code must be <= 50
I_N_P_U_T = (range(globals()[list(globals())[0]]))
print I_N_P_U_T
print '11111111111111111111111111111111111111111111111111111111111111111111111111111'
print (globals()[list(globals())[1]])
print '11111111111111111111111111111111111111111111111111111111111111111111111111111'
print globals()[list(globals())[2]]
print '11111111111111111111111111111111111111111111111111111111111111111111111111111'

P_A_S_S_W_O_R_D = open('./password','r').read()

assert LEN_PASS >= 1
assert LEN_PASS == len(I_N_P_U_T)
for i in range(LEN_PASS):
	if I_N_P_U_T[i] != P_A_S_S_W_O_R_D[i]:
		from sys import exit
		print 'wrong'
		exit() # Wrong

# FLAGGGGGGGGGGGGGGGGGGGGGGGG
print 'Here is your flag:',open('./flag','r').read()

(list(globals()[list(globals())[8]]))