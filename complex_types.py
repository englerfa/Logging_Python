import numpy as np
import scipy.sparse as sp

# simplified code from scikit: https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/datasets/svmlight_format.py#L40
def np_float_constructor(dtype=np.float64):
    return dtype([1])

# stateful func
