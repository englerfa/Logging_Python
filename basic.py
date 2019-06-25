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

    def variable_arguments(*argv):
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

    def get_telnr_from_dictionary(self, d, e):
        if d != None and len(d) > 0 and len(e)>0:
            print("get_element_from_dictionary(d,e) is being called from", D.__name__, "with" , d)
            return d[e]
        else:
            print("get_element_from_dictionary(d,e) is being called from", D.__name__, "with empty set")





