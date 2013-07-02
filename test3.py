import sys

from numba import autojit, jit

autojit = autojit if int(sys.argv[1]) else lambda x: x
jit = jit if int(sys.argv[1]) else lambda x: x

@jit('void()')
def f():
    x = [1, 2, 3]
    i = 0
    for elem in x:
        i = i + 1

print f.lfunc
print f()
