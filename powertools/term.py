
'''
terminal colors
'''

from termcolor import colored
from functools import partial

cprint = lambda color, bold, *args: colored( ''.join(str(s) for s in args), color, attrs=['bold'] if bold else [])

white   = partial( cprint, 'white',  True )
red     = partial( cprint, 'red',    True )
green   = partial( cprint, 'green',  True )
blue    = partial( cprint, 'blue',   True )
pink    = partial( cprint, 'pink',   True )
yellow  = partial( cprint, 'yellow', True )
cyan    = partial( cprint, 'cyan',   True )

dwhite  = partial( cprint, 'white',  False )
dred    = partial( cprint, 'red',    False )
dgreen  = partial( cprint, 'green',  False )
dblue   = partial( cprint, 'blue',   False )
dpink   = partial( cprint, 'pink',   False )
dyellow = partial( cprint, 'yellow', False )
dcyan   = partial( cprint, 'cyan',   False )

