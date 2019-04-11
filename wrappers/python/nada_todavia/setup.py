from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

module_fparam = Extension('fparams',
                          ["fparams.pyx"]
)

extensions = [module_fparam]

setup(
    ext_modules = cythonize(extensions)
)

