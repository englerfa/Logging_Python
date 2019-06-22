

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
    def __init__(self, name1, name2):
        Person.__init__(name1)
        Vehicle.__init__(name2)

    def get_name(self):
        return self.name