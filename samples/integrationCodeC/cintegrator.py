 


        


from os.path import abspath, dirname, join
import ctypes
from ctypes import cdll


class Cintegrator(object):
        def __init__(self, libraryname):
        # LOAD LIBRARY
                here = dirname(abspath(__file__))
                path = join(here, libraryname)
                self.lib = cdll.LoadLibrary(path)

        
        


