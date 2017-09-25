#-- powertools.__init__

"""--- power.tools and power.test
general-purpose utility and testing library
"""

#----------------------------------------------------------------------#

# todo: metaclass that allows composition of classes using the | operator

from .setup.arguments import __version__

from .export import export          # decorator

from .meta import classproperty     # decorator
from .meta import assertion         # context manager

from .logging import AutoLogger     # class


#----------------------------------------------------------------------#
