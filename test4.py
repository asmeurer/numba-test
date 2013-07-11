from numba import jit

@jit('void(float64[:])')
def g(X):
    for i in X:
        pass


# @jit('void()')
# def rangeloop():
#     for i in h(10):
#         pass
#
# def h():
#     return [1, 2, 3]

@jit('void()')
def f():
    x = range(10)
    for i in x:
        pass
