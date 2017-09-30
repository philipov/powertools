#!python
#-- setup.py -- powertools

from setuptools import setup
from powertools.setup.arguments import kwargs
import os

with open( os.path.join( os.path.dirname( __file__ ), 'description.rst' ) ) as r_file :
    readme = r_file.read()

setup( **kwargs, long_description=readme )

#----------------------------------------------------------------------#
