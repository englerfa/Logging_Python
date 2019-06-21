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

    def get_first_from_list(self, l):
        if len(l) > 0:
            print("get_first(l) is being called with", l)
            return l[0]
        else:
            print("get_first(l) is being called with empty list")

    def multiple_calls(self, first):
        print("multiple_calls(self, first) is being called from", self.class_name)
        print_text()

    class A1:
        class_name = "inner class A1"
        def print_text(self):
            print("print_text(self) is being called from", self.class_name)



class B:
    class_name = "B"
    def swap(self, a, b):
        print("swap(self,a,b) is being called")
        (b, a) = (a, b)

    @staticmethod
    def static_method():
        print("static_method() is being called")













