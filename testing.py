# 13.06.2019

import main
import main_basic
import main_basic_nested
import logging              # if we import this module, then logging is automatically activated


# TODO catch exceptions. Print error instead.
# TODO get all methods automatically and call all them with random parameters.



# Test function/method calls
main_basic.print_example()          # function

main_basic_a = main_basic.A()       # create object/instance
main_basic_a.add_numbers(3,5)       # method

main.print_example()
main.add_five_global(5)

main_A = main.A()
main_A.print_example()
main_A.add_numbers(4,69)
main_A.add_numbers1(3,4,5)
main_A.swap(3,5)
main_A.outer_funtion()
main_A.method_calls()
main_A.arg_object(main.B)
main_A.get_balance()
main_A.arg_set(4)

main.A.static_method()

main_B = main.B()
main_B.add_numbers(2,4)
main_B.print_simple()

main_B_C = main.B.C()
main_B_C.print_simple()


main_basic_nested.f0()

main_basic_nested_A = main_basic_nested.A()
main_basic_nested_A.fA()

main_basic_nested_B = main_basic_nested.B()
main_basic_nested_B.fB()

main_basic_nested_B_C = main_basic_nested.B.C()
main_basic_nested_B_C.fC()









