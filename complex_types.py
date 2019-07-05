import numpy as np


# simplified code from scikit:
# https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/svmlight_format.py#L40
def np_float_constructor(dtype=np.float64):
    return dtype([1])

# stateful func


# function calls function
def foo2(a):
    return a*2


def foo1(a):
    return foo2(a) + 1


# run everything
def run():
    np_float_constructor()
    np_float_constructor(np.int64)
    foo2(1)
