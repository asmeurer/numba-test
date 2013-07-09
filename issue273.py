from numba import jit, u4, void

@jit(void(u4[:]))
def fail(ptr):
    for i in range(10):
        j = ptr[i]
        while j < ptr[i + 1]:
            j += 1
