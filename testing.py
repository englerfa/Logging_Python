# 13.06.2019

import main
import main_basic
import main_basic_nested
import logging              # if we import this module, then logging is automatically activated


# TODO catch exceptions. Print error instead.
# TODO get all methods automatically and call all them with random parameters.



# Test function/method calls
main_basic.print_example()          # function

main_basic_a = main_basic.A()
main_basic_a.add_numbers(3,5)       # method

main.print_example()
main.add_five_global(5)

main_A = main.A
main.A.print_example(0)
main.A.add_numbers(0,4,69)
main.A.add_numbers1(0,3,4,5)
main.A.swap(0,3,5)
main.A.static_method()
main.A.outer_funtion(0)
main.A.method_calls(0)
main.A.arg_object(0, main.B)
main.A.get_balance(main_A)
main.A.arg_set(main_A,4)

main.B.add_numbers(0,2,4)
main.B.print_simple(0)
main.B.C.print_simple(0)

main_basic_nested.f0()
main_basic_nested.A.fA(0)
main_basic_nested.B.fB(0)
main_basic_nested.B.C.fC(0)









