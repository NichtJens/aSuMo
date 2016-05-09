
from types import ModuleType

class submod1(ModuleType):
    class foo:
        pass

class submod2(ModuleType):
    class bar:
        pass


from asumo import add_submodule

add_submodule(submod1, __name__)
add_submodule(submod2, __name__)



