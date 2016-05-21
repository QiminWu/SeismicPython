from seispy.core import *

class Arrival(DbParsable):
    '''
    A container class for phase data.
    '''
    def __init__(self, *args, **kwargs):
        self.attributes = ()
        if len(args) == 1:
            import os
            import sys
            try:
                sys.path.append('%s/data/python' % os.environ['ANTELOPE'])
            except ImportError:
                #Presumably in the future an alternate parsing method
                #would be implemented for an object other than a Dbptr.
                raise ImportError("$ANTELOPE environment variable not set.")
            self._parse_Dbptr(args[0])
        else:
            self.sta = args[0]
            self.attributes += ('sta',)
            self.time = args[1]
            self.attributes += ('time',)
            self.iphase = args[2]
            self.attributes += ('iphase',)
            for attr in ('chan', 'deltim', 'qual', 'arid', 'tt_calc', 'predarr'):
                if attr in kwargs:
                    setattr(self, attr, kwargs[attr])
                else:
                    setattr(self, attr, None)
                self.attributes += (attr,)

