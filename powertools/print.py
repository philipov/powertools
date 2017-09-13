#-- powertools.out

'''
pretty print functions
'''

#-------------------------------------------------------------------------------------------------#

from pprint import PrettyPrinter
_pprinter   = PrettyPrinter()
pprint      = _pprinter.pprint
pformat     = _pprinter.pformat


def add_pprint(cls):
    _pprinter._dispatch[cls.__repr__] = cls.__pprint__


#-------------------------------------------------------------------------------------------------#

#ToDo: 'tprint' - write to multiple streams

def dictprint( d ) :
    list( print( '{:<12}:'.format(str(key)), value ) for key, value in d.items( ) )

def listprint( l ) :
    list( print( value ) for value in l )

def rprint( struct, i=0, quiet=False ) :
    #ToDo: return a string

    result = ""
    if isinstance( struct, list ) : # loop over list
        for value in struct :
            if isinstance( value, dict ) \
                    or isinstance( value, list ) : # recurse on subsequence
                result += rprint( value, i + 2, quiet )

            else :
                line = ' '*i + "- " + str( value )
                result += line + "\n"
                print( line ) if quiet is False else None

    elif isinstance( struct, dict ) : # loop over dict
        for (key, value) in struct.items( ) :
            line = ' '*i + "{:<12}: ".format(str(key))
            result += line
            print( line, end='' ) if quiet is False else None

            if isinstance( value, dict ) \
                    or isinstance( value, list ) : # recurse on subsequence
                print( "" ) if quiet is False else None
                result += "\n"
                result += rprint( value, i + 2, quiet )

            else :
                result += str( value ) + "\n"
                print( str( value ) ) if quiet is False else None

    return result


#-------------------------------------------------------------------------------------------------#

