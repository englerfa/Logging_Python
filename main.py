import basic
import nested
import autolog              # if we import this module, then logging is automatically activated

modules_to_log = [basic, nested]


autolog.add_module(basic)
autolog.traverse_modules(modules_to_log)
autolog.execute_monkey_patching()


# Call functions from module main_basic
basic.print_text()

# Call class methods from module main_basic
obj_A = basic.A()           # create new object
obj_A.print_text()
obj_A.add_numbers(3,5)
obj_A.add_numbers(-3,-5)
obj_A.add_numbers(first=3,second=5)
obj_A.add_numbers(second=3,first=5)
obj_A.add_numbers(*[1,2])
obj_A.add_numbers1(3,5,99)
obj_A.get_balance()
obj_A.multiple_calls(7)

obj_A1 = obj_A.A1()              # create new object
obj_A1.print_text()

obj_B = basic.B()           # create new object
obj_B.swap(3,5)
basic.B.static_method()






# Call functions from module main_nested
nested.f0()

# Call class methods from module main_nested
obj_A = nested.A()              # create new object
obj_A.fA()

obj_B = nested.B()              # create new object
obj_B.fB()

obj_C = nested.B.C()            # create new object
obj_C.fC()




