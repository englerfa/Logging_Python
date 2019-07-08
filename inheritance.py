

class Person:
    # Constructor
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


# Inherited or Sub class
class Employee(Person):
    def is_employee(self):
        return True



class Vehicle:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Combined(Person, Vehicle):
    def __init__(self, name1, name2):  # fixed wrong super() call
        super(Combined, self).__init__(name1).__init__(name2)
        # both parent classes have the same attribute name, which is then incorrectly shadowed! So the code is incorrect

    def get_name(self):
        return self.name


def run():
    p1 = Person("Jack")  # create new object
    p1.get_name()
    p1.is_employee()

    print()
    p2 = Employee("Jane")
    p2.get_name()
    p2.is_employee()

    print()
    p3 = Combined("Emily", "Citroen")
    p3.get_name()
