
import sys

def add_submodule(submod, parentname):
    name = submod.__name__
    sys.modules[parentname + "." + name] = submod(name)



