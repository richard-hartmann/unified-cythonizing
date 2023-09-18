# unified-cythonizing
Unify building cython extension -- pip install, poetry install, poetry build and development builds

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

> :large_blue_diamond: The goal of this repository is to unify building cython extensions 
> from command line and by default on installation.
> The main ingredient is the `build_ext.py` script which has a CLI and provides the necessary 
> hooks needed by a build backend.
> Currently the `setuptools` legacy backend and the [poetry](https://python-poetry.org/) 
> backend have been tested. 


# Preparation

1.  Add the `build`-key to the projects `pyproject.toml`.
    ```
     build = 'build_ext.py'
    ```
    Note that this key is not included in 
    [PEP 621](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/).
    According to [How to use Cython with Poetry? - stackoverflow](https://stackoverflow.com/questions/63679315/how-to-use-cython-with-poetry)
    the `build`-key appears to be an undocumented feature in poetry. Well is works!

2.  Include the [`build_ext.py`](https://github.com/richard-hartmann/unified-cythonizing/blob/main/build_ext.py) 
    script in your project (root location, just as the `pyproject.toml`) 
3.  Add your extensions to the `build_ext.py` file which will look similar to:
    ```python
    foo_c = Extension(
    # the
    "foo.foo_c",
    sources=["./foo_c_ext/foo_c.pyx"],
    extra_compile_args=["-O3"],
    )
    
    bar_c = Extension(
        # the
        "foo.bar.bar_c",
        sources=[
            "./foo_c_ext/bar_c.pyx",
        ],
        extra_compile_args=["-O3"],
    )
    
    list_of_ext = [foo_c, bar_c]
    ```

# Usage

## building cython extension

The cython extension is now build on many occasions.

### local build from command line 

Simply run

> $ python3 build_ext.py

to trigger an explicit build of your extension.
Note that sometimes cython does not regenerate the c/cpp files even though it would be appropriate.
In that case remove such generated files with `python3 build_ext.py clean` (see below).
Furthermore, the files for the extension are searched for relative to the location of the 
`build_ext.py` script, i.e. the *Present Working Directory* is irrelevant.

### poetry install

Invoking 

> $ poetry install

from somewhere within your project will build (including the cython parts) and install the project.

### poetry build

Invoking 

> $ poetry build

from somewhere within your project will build (including the cython parts) the project.

### pip install

Invoking 

> $ pip install .

from the root directory of your will build (including the cython parts) and install the project.

## clean up

To remove files that have been generated during the build process, type:

> $ python3 build_ext.py clean

This will remove 
* `build`
* `dist`
* c/cpp files generated from `.pyx` files
* library files of the extension, i.e., `.so` files

There is an `--yes` flag to remove files without asking. 

# License - BSD (3 clause)

Copyright 2023 Richard Hartmann

Redistribution and use in source and binary forms, with or without modification, are permitted 
provided that the following conditions are met:

1.  Redistributions of source code must retain the above copyright notice, this list of 
    conditions and the following disclaimer.

2.  Redistributions in binary form must reproduce the above copyright notice, this list 
    of conditions and the following disclaimer in the documentation and/or other materials 
    provided with the distribution.

3.  Neither the name of the copyright holder nor the names of its contributors may be 
    used to endorse or promote products derived from this software without specific 
    prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR 
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR 
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN 
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.