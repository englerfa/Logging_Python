# 07.06.2019 Proof of concept for recursion.

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