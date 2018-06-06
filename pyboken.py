"""Minimal Python 2 shim around shiboken and pysideuic calls

DOCUMENTATION
    A quick wrapper to help dealing with shiboken and pysideuic calls.

    Default order:
        - PySide2
        - PySide
        
    Works off of the defualt pysideuic and shiboken calls.
    
    Ex:
    
    from pyboken import shiboken, pysideuic
    
    all calls use this and resolve to their pyside or pyside2 equilivents.


LICENSE

    See end of file for license (MIT, BSD) information.
"""

import sys

#Enable support for from pyboken import *
__all__ = []

_pyside2_common_members = [{'shiboken2':'shiboken'}, {'pyside2uic':'pysideuic'}]
_pyside_common_members = [{'shiboken':'shiboken'}, {'pysideuic':'pysideuic'}]

ate = sys.modules[__name__]

#Create shim depending on pyside version.
if 'PySide2' in sys.modules:
    print 'WE ARE IN PYSIDE 2'

    for entry in _pyside2_common_members:
        for import_name, name in dict(entry).iteritems():

            try:
                submodule = __import__(import_name)
            except ImportError:
                continue

            setattr(ate, name, submodule)

            our_submodule = getattr(ate, name)

            # Enable import *
            __all__.append(name)

            # Enable direct import of submodule,
            # e.g. import ate_pyboken.shiboken
            sys.modules[__name__ + "." + name] = our_submodule


else:
    for entry in _pyside_common_members:
        for import_name, name in dict(entry).iteritems():

            try:
                submodule = __import__(import_name)
            except ImportError:
                continue

            setattr(ate, name, submodule)


            our_submodule = getattr(ate, name)

            # Enable import *
            __all__.append(name)

            # Enable direct import of submodule,
            # e.g. import ate_pyboken.shiboken
            sys.modules[__name__ + "." + name] = our_submodule


# The MIT License (MIT)
#
# Copyright (c) 2016-2018 Michael McEachern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.