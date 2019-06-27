import basic
import basic2
import nested
import inheritance

import autolog              # if we import this module, then logging is automatically activated

autolog.add_modules( [basic, basic2, nested, inheritance] )
autolog.run()


basic.print_text()

obj_A = basic.A()           # create new object
obj_A.print_text()

obj_A.add_numbers(3,5)
obj_A.add_numbers(-3,-5)
obj_A.add_numbers(3,5j)
obj_A.add_numbers(first=3,second=5)
obj_A.add_numbers(second=3,first=5)
obj_A.add_numbers(*[1,2])
obj_A.add_numbers(**{'second':1,'first':2})

obj_A.add_numbers1(3,5,99)
obj_A.get_balance()
obj_A.multiple_calls(7)

obj_A1 = obj_A.A1()              # create new object
obj_A1.print_text()

obj_B = basic.B()           # create new object
obj_B.swap(3,5)
basic.B.static_method()
print()

obj_D = basic.D()              # create new object
# Tuple
t = 12345, 54321, 'hello!'
obj_D.get_element(t)
obj_D.get_element(None)
# List
numbers = [1,2,3]
obj_D.get_first_from_list(numbers)
obj_D.get_first_from_list(numbers[1:2])
obj_D.get_first_from_list([])
# Set
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
obj_D.is_element_in_set(basket, 'orange')
obj_D.is_element_in_set(basket, '')
obj_D.is_element_in_set(None, 'orange')
obj_D.is_element_in_set(None, '')
# Dictionary
tel = {'jack': 4098, 'sape': 4139}
obj_D.get_nr_from_dictionary(tel, 'jack')
obj_D.get_nr_from_dictionary(tel, '')
obj_D.get_nr_from_dictionary(None, 'jack')
obj_D.get_nr_from_dictionary(None, '')
print()


# Call functions from module main_nested
nested.f0()

# Call class methods from module main_nested
obj_A = nested.A()              # create new object
obj_A.fA()

obj_B = nested.B()              # create new object
obj_B.fB()

obj_C = nested.B.C()            # create new object
obj_C.fC()
print()






p1 = inheritance.Person("Jack")              # create new object
p1.get_name()
p1.is_employee()

print()
p2 = inheritance.Employee("Jane")
p2.get_name()
p2.is_employee()

print()
#p3 = inheritance.Combined("Emily", "Citroen")




basic2.add_numbers(3,5)
e1 = basic2.E()
e1.no_default_parameter(7)
e1.one_default_parameter(3)
e1.one_default_parameter()

e2 = basic2.E()
e2.two_default_parameters(3)
e2.two_default_parameters(3,4)
e2.two_default_parameters(3,4,5)

print()
e1.variable_argument([])
e1.variable_argument([1])
e1.variable_argument([1,2,3])
print()
e1.normal_variable_argument(4, [1,2,3])
print()
e1.default_variable_argument([1,2,3])
e1.normal_default_variable_argument(4, [1,2,3])
e1.normal_default_variable_argument(4, [1,2,3],3)
print()
e1.variable_kwargs()
e1.variable_kwargs(a ='A')
e1.variable_kwargs(a ='A', b ='B', c='C')





