from numba import jit

@jit('void()')
def f():
    x = range(10)
    for i in x:
        pass
