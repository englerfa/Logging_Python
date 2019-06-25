
def add_numbers(first, second):
    print("add_numbers(self,first,second) is being called")
    return first + second

class E:

    def no_default_parameter(self, d):
        print("default_parameter() is being called from", E.__name__, "with", d)

    def one_default_parameter(self, d=5):
        print("default_parameter(d=5) is being called from", E.__name__, "with", d)

    def two_default_parameters(self, d, e=6, f=7):
        print("default_parameter(d, e=6, f=7) is being called from", E.__name__, "with", d,e,f)






