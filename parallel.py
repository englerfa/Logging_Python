import math
import joblib


def compute_sqrt():
    print("compute_sqrt() is being called")
    return [math.sqrt(i ** 2) for i in range(10)]



def compute_sqrt_parallel():
    print("compute_sqrt() is being called")
    return joblib.Parallel(n_jobs=2)(joblib.delayed(math.sqrt)(i ** 2) for i in range(10))



def run():
    compute_sqrt()
    compute_sqrt_parallel()