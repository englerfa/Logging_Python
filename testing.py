# 13.06.2019

import main
import main_basic
import main_basic_nested
import logging              # if we import this module, then logging is automatically activated


# TODO catch exceptions. Print error instead.
# TODO get all methods automatically and call all them with random parameters.





# Test function/method calls
# Module main
#main.print_text()
obj_A = main.A()           # create new object
obj_A.print_text()
obj_A.add_numbers(3,5)
obj_A.add_numbers1(3,5,99)
obj_A.get_balance()
obj_A.multiple_calls(7)
obj_A.swap(3,5)

obj_B = obj_A.B()           # create new object
obj_B.print_text()


main.F.static_method()

obj_F = main.F()            # create new object
obj_F.arg_set(5)




# Module
main_basic.print_text()          # function
main_basic_a = main_basic.A()       # create object/instance
main_basic_a.add_numbers(3,5)       # method

# Module
main_basic_nested.f0()

main_basic_nested_A = main_basic_nested.A()
main_basic_nested_A.fA()

main_basic_nested_B = main_basic_nested.B()
main_basic_nested_B.fB()

main_basic_nested_B_C = main_basic_nested.B.C()
main_basic_nested_B_C.fC()









