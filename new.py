import numbers


def add_numbers(first, second):
    print("add_numbers(first,second) is being called")
    return first + second


def use_library_functions():
    print("use_library_functions() is being called")
    q = numbers.Rational
    q.numerator = 1
    q.denominator = 7
    q.conjugate(1)
    return(f"q={q.numerator}/{q.denominator}")

