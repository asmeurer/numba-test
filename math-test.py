#!/usr/bin/env python
import time
import math
from numba import autojit
import numpy as np

def sqrt_test(N):
    ans = 0
    A = np.arange(N)
    for i in A:
        ans = math.sqrt(i + ans)

sqrt_test_numba = autojit(sqrt_test)

def main():
    N = 10000
    print 'sqrt python: ',
    t = time.time()
    sqrt_test(N)
    print time.time() - t

    print 'sqrt numba: ',
    t = time.time()
    sqrt_test_numba(N)
    print time.time() - t

if __name__ == '__main__':
    main()
