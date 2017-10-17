#-- composable.py

'''
composable function decorator
'''

from powertools import composable

#----------------------------------------------------------------------------------------------#

@composable
def A(a):
    return a + ' A'

@composable
def B(b):
    return b + ' B'

def C(c):
    return c + ' C'

D = A | B | C
E = B | C | A

print('D: ', D('D'))

print('E: ', E('E'))

print('_: ', (B | C | A)('_'))

#----------------------------------------------------------------------------------------------#

