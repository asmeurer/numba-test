import sys

from numba import autojit

autojit = autojit if int(sys.argv[1]) else lambda x: x

@autojit
def f(x):
    i = 0
    for elem in x:
        i += 1

print f(range(10))
