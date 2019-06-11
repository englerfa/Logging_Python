#06.05.2019 Proof of concept. Different cases of functions


def add_five_global(value):
    return value + 5

def print_example():
    print("print_example() is being called")

class A:
    balance = 5

    name = "global variable"    # global scope. We dont want to log it.
    # -> Describe sharply what we log and what not.
    # All functions are logged. That is everything that is defined with 'def'
    # Here we log:
    # - the name
    # - the argument names
    # - the argument values
    # - the return types

    def print_example(self):
        print("print_example(self) is being called")

    @staticmethod
    def static_method():
        pass

    def add_numbers(self, first, second):
        print("add_numbers(self,first,second) is being called")
        return first + second

    def add_numbers1(self, first, second, third):
        print("add_numbers(self, first, second, third) is being called")
        return first + second

    def get_balance(self):
        print("get_balance(self) is being called")
        return self.balance

    def swap(self, a, b):
        print("swap(self,a,b) is being called")
        (b, a) = (a, b)


    def outer_funtion(self):
        print("outer_function(self) is being called")
        def inner_function():
            print("inner_function() is being called")
        inner_function()


    def foo(a, *, b: int, **kwargs):
        pass

    def foo1(a, b, *, c, d=10):
        pass



class B:

    def print_simple(self):
        print("print_simple(self) is being called")

    #same function as in class A
    def add_numbers(self, first, second):
        print("add_numbers(self, first, second) is being called")
        sum = first + second
        return sum


    # class inside of class
    class C:
        def print_simple(self):
            print("print_simple(self) is being called")