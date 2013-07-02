from numba import jit

@jit('void()')
def f():
    x = range(100)
    for i in x:
        pass
