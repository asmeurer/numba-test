#!/usr/bin/env python
from __future__ import division

import sys
import time
import math
from numba import autojit

def sqrt_test(N):
    ans = 0
    for i in range(N):
        ans = math.sqrt(i) + ans

def log_test(N):
    ans = 1
    for i in range(1, N):
        ans = math.log(i) + ans

def exp_test(N):
    ans = 0
    for i in range(N):
        ans = math.exp(i/100) + ans

def main():
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        N = 10000

    for name in [
        'sqrt',
        'log',
        'exp',
    ]:
        print '%s python: ' % name,
        func = globals()[name + '_test']
        t = time.time()
        func(N)
        print time.time() - t

        print '%s numba: ' % name,
        func = autojit(func)
        t = time.time()
        func(N)
        print time.time() - t


if __name__ == '__main__':
    main()
