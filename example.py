#!/usr/bin/env python

import example_mod.submod1 as sm1
from example_mod import submod2 as sm2

print sm1, sm1.foo()
print sm2, sm2.bar()



