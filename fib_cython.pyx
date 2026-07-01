cimport cython

@cython.cdivision(True)
def fibonacci_cython(int n):
    cdef int i

    if n <= 1:
        return n
    
    a, b = 0, 1

    for i in range(2, n + 1):
        temp = a + b
        a = b
        b = temp

    return b