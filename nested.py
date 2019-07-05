
def f0():
    pass

class A:
    def fA(self):
        def fA1():
            pass

class B:
    def fB(self):
        pass

    class C:
        def fC(self):
            pass

    class D:
        class E:
            pass

def run():
    # Call functions from module main_nested
    f0()

    # Call class methods from module main_nested
    obj_A = A()  # create new object
    obj_A.fA()

    obj_B = B()  # create new object
    obj_B.fB()

    obj_C = B.C()  # create new object
    obj_C.fC()
    print()