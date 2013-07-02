import sys

from numba import autojit

autojit = autojit if int(sys.argv[1]) else lambda x: x

@autojit
def f(x):
    acc = 0
    i = 0
    for elem in x:
        i += 1
    return acc

print f(range(10))
