from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="fibonacci_cython",
        sources=["fib_cython.pyx"],
        extra_compile_args=["-O3"],
        extra_link_args=["-O3"],       
    ),
    Extension(
        name="fibonacci_pure",
        sources=["fib_pure.py"],
        extra_compile_args=["-O3"],
        extra_link_args=["-O3"]
    ),
]

setup(
    name='Indently',
    ext_modules=cythonize(
        module_list=extensions,
        compiler_directives={
            'language_level': 3,
            'boundscheck': False,
            'wraparound': False,
            'cdivision': True,
        },
    ),
    zip_safe=False,
    install_requires=[
        'cython',
    ],
)