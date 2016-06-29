"""
.. module:: seispy
.. moduleauthor:: Malcolm White malcolcw@usc.edu
.. versionadded:: 0.0alpha
"""

import os
import sys

__all__ = []

try:
    sys.path.append('%s/data/python' % os.environ['ANTELOPE'])
    import antelope
    __all__ += ["antelope"]
except ImportError:
    _ANTELOPE_DEFINED = False
_ANTELOPE_DEFINED = True

__all__ += ["_ANTELOPE_DEFINED"]

_INSTALL_DIR = os.path.split(__file__)[0]
_DATA_DIR = "%s/data" % _INSTALL_DIR
