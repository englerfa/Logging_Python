# 07.06.2019 Proof of concept for recursion.
import  main_nested
import logging

# Call functions from module main_nested
main_nested.f0()

# Call class methods from module main_nested
obj_A = main_nested.A()              # create new object
obj_A.fA()

obj_B = main_nested.B()              # create new object
obj_B.fB()

obj_C = main_nested.B.C()            # create new object
obj_C.fC()







