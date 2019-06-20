'''
Different function/method calls to test if all of them are logged correctly.
'''

def print_text():
    print("print_text() is being called")

class A:
    balance = 5
    class_name = "A"

    def print_text(self):
        print("print_text(self) is being called from" , self.class_name)

    def add_numbers(self, first, second):
        print("add_numbers(self,first,second) is being called from", self.class_name)
        return first + second

    def add_numbers1(self, first, second, third):
        print("add_numbers1(self, first, second, third) is being called from", self.class_name)
        return first + second

    def get_balance(self):
        print("get_balance(self) is being called from", self.class_name)
        return self.balance

    def multiple_calls(self, first):
        print("multiple_calls(self, first) is being called from", self.class_name)
        print_text()


    def swap(self, a, b):
        print("swap(self,a,b) is being called")
        (b, a) = (a, b)

    # nested class
    class B:
        class_name = "B"
        def print_text(self):
            print("print_text(self) is being called from", self.class_name)



class F:
    def arg_set(self, d=5):
        print("arg_set(self, d=5) is being called" , d)


    def outer_funtion(self):
        print("outer_function(self) is being called")
        def inner_function():
            print("inner_function() is being called")
        inner_function()

    @staticmethod
    def static_method():
        pass

    def arg_object(self, a):
        print("arg_obj(self, a) is being called")


    def foo(a, *, b: int, **kwargs):
        pass

    def foo1(a, b, *, c, d=10):
        pass












