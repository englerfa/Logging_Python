def print_text():
    print("print_text() is being called")

class A:
    static_field = 10

    def __init__(self):
        self.balance = 5

    def print_text(self):
        print("print_text(self) is being called from" , A.__name__)

    def add_numbers(self, first, second):
        print("add_numbers(self,first,second) is being called from", A.__name__)
        return first + second

    def add_numbers1(self, first, second, third):
        print("add_numbers1(self, first, second, third) is being called from", A.__name__)
        return first + second

    def get_balance(self):
        print("get_balance(self) is being called from", A.__name__)
        return self.balance + self.static_field

    def multiple_calls(self, first):
        print("multiple_calls(self, first) is being called from", A.__name__)
        print_text()

    class A1:
        class_name = "inner class A1"
        def print_text(self):
            print("print_text(self) is being called from", A.__name__)



class B:
    def swap(self, a, b):
        print("swap(self,a,b) is being called from", B.__name__)
        (b, a) = (a, b)

    @staticmethod
    def static_method():
        print("static_method() is being called from", B.__name__)

    def variable_arguments(self, *argv):
        print("variable_arguments() is being called from", B.__name__)
        for arg in argv:
            print(arg)


class D:
    def get_element(self, data):
        if data != None and len(data) > 0:
            print("get_element(data) is being called from", D.__name__, "with" , data)
            return data[0]
        else:
            print("get_element(s,e) is being called from", D.__name__, "with empty set")

    def get_first_from_list(self, l):
        if l != None and len(l) > 0:
            print("get_first_from_list(l) is being called from", D.__name__, "with", l)
            return l[0]
        else:
            print("get_first_from_list(l) is being called from", D.__name__, "with empty list")

    def is_element_in_set(self, s, e):
        if s != None and len(s) > 0:
            print("is_element_in_set(s,e) is being called from", D.__name__, "with" , s)
            return e in s
        else:
            print("is_element_in_set(s,e) is being called from", D.__name__, "with empty set")

    def get_nr_from_dictionary(self, d, e):
        if d != None and len(d) > 0 and len(e)>0:
            print("get_nr_from_dictionary(d,e) is being called from", D.__name__, "with" , d)
            return d[e]
        else:
            print("get_nr_from_dictionary(d,e) is being called from", D.__name__, "with empty set")


def run():
    print_text()

    obj_A = A()  # create new object
    obj_A.print_text()

    obj_A.add_numbers(3, 5)
    obj_A.add_numbers(-3, -5)
    obj_A.add_numbers(3, 5j)
    obj_A.add_numbers(first=3, second=5)
    obj_A.add_numbers(second=3, first=5)
    obj_A.add_numbers(*[1, 2])
    obj_A.add_numbers(**{'second': 1, 'first': 2})

    obj_A.add_numbers1(3, 5, 99)
    obj_A.get_balance()
    obj_A.multiple_calls(7)

    obj_A1 = obj_A.A1()  # create new object
    obj_A1.print_text()

    obj_B = B()  # create new object
    obj_B.swap(3, 5)
    B.static_method()
    print()

    obj_D = D()  # create new object
    # Tuple
    t = 12345, 54321, 'hello!'
    obj_D.get_element(t)
    obj_D.get_element(None)
    # List
    numbers = [1, 2, 3]
    obj_D.get_first_from_list(numbers)
    obj_D.get_first_from_list(numbers[1:2])
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
