
from numba import autojit

@autojit
def test(a, b):
    return (a < b) - (a > b)

print test(1, 2)
print test(2, 1)
print test(True, False)
print test(1, True)
