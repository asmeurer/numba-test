- `"%d" % i` does not work, `"%d" % (i,)` does work
- Explicit loops vs. masks
- Keyword arguments (calling `f(1, b=2)` does not work, `f(1, 2)` does work)
- Multiple enumeration (`for i, j in enumerate(X)` does not work, setting `i =
  0`, `for j in X`, and adding `i += 1` to the end does work; `for i, j in
  stuff` does not work, `for i_j in stuff: i = i_j[0]; j = i_j[1]` does work)
- Unpacking (`i, j = stuff` does not work, `i = stuff[0]; j = stuff[1]` does
  work)
- `a = b = c` does not work (considered unpacking).
- Numba doesn't correctly change the type info from int to bool (see test2.py)
- `jit`ed functions cannot be defined out of order
