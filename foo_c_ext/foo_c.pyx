#cython: language_level=3

cimport cython
from libc.math cimport fabs

cpdef double crazy_abs_value(double x):
    return fabs(x)