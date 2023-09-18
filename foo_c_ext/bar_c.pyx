#cython: language_level=3

cimport cython

cpdef double crazy_square(double x):
    return x*x