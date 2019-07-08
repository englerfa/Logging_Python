
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



    def variable_argument(self, *argv):
        print("variable_argument(*argv) is being called from", E.__name__)

    def variable_normal_argument(self, *argv, a):
        print("variable_normal_argument(*argv, a) is being called from", E.__name__)

    def normal_variable_argument(self, a, *argv):
        print("normal_variable_argument(a, *argv) is being called from", E.__name__)

    # this is not valid Python code - default arguments have to be behind non-default
    # SyntaxError: non-default argument follows default argument
    #def default_variable_argument(self, a=7, *argv):
    #    print("normal_variable_argument(a, *argv) is being called from", E.__name__)

    def normal_default_variable_argument(self, a, *argv, b=7):
        print("normal_variable_argument(a, *argv) is being called from", E.__name__)



    def variable_kwargs(self, **kwargs):
        print("variable_kwargs(**kwargs) is being called from", E.__name__)

    def normal_variable_kwargs(self, a, **kwargs):
        print("normal_variable_kwargs(**kwargs) is being called from", E.__name__)


def run():
    add_numbers(3, 5)
    e1 = E()
    e1.no_default_parameter(7)
    e1.one_default_parameter(3)
    e1.one_default_parameter()

    e2 = E()
    e2.two_default_parameters(3)
    e2.two_default_parameters(3, 4)
    e2.two_default_parameters(3, 4, 5)

    print()
    e1.variable_argument([])
    e1.variable_argument([1])
    e1.variable_argument([1, 2, 3])
    print()
    e1.normal_variable_argument(4, [1, 2, 3])
    print()
    #e1.default_variable_argument([1, 2, 3])
    e1.normal_default_variable_argument(4, [1, 2, 3])
    e1.normal_default_variable_argument(4, [1, 2, 3], 3)
    print()
    e1.variable_kwargs()
    e1.variable_kwargs(a='A')
    e1.variable_kwargs(a='A', b='B', c='C')

