# unified-cythonizing
Unify building cython extension -- pip install, poetry install, development builds

# Disclaimer

This suggestion for building cython extensions is based on use cases from a few projects. 
Most likely, there are many pitfalls.
The aim is to share experiences and improve the functionality together.

# Goal

When doing numerics with python occasionally you will find yourself in a position where 
your newly developed algorithm needs speedup.
Of course, as a first step you should try [Numba](https://numba.pydata.org/), an open source 
JIT compiler that translates a subset of Python and NumPy code into fast machine code.

However, if you want a pre-compiled version you can use [Cython](https://cython.org/).
For straight forward local development everything is well explained in the documentation.
Once you want to publish your code so other can simply install your package, it is highly 
desirable that cytonizing and building happens upon installation.
In former days, where instructions on package installation were given in a `setup.py` file, 
the `distutils` magic for building extension could be triggered by invoking something like 
`$ python setup.py build_ext --inplace`.

Modern Python packages usually contain a 
[`pyproject.toml`](https://pip.pypa.io/en/stable/reference/build-system/pyproject-toml/) 
file to manage packaging (general information, dependencies, build system requirements, 
build backend ...).

> :large_blue_diamond: 