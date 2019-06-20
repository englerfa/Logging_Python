import main_basic
import logging              # if we import this module, then logging is automatically activated


# Call functions from module main_basic
main_basic.print_text()

# Call class methods from module main_basic
obj_A = main_basic.A()           # create new object
obj_A.print_text()
obj_A.add_numbers(3,5)
obj_A.add_numbers(-3,-5)
obj_A.add_numbers(first=3,second=5)
obj_A.add_numbers(second=3,first=5)
obj_A.add_numbers1(3,5,99)
obj_A.get_balance()
obj_A.multiple_calls(7)

obj_A1 = obj_A.A1()              # create new object
obj_A1.print_text()

obj_B = main_basic.B()           # create new object
obj_B.swap(3,5)
main_basic.B.static_method()












