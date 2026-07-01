import sys
import timeit

from fib import fibonacci as py_fibonacci

try:
    from fibonacci_pure import fibonacci as cython_pure_fibonacci
except ImportError as exc:
    cython_pure_fibonacci = None
    cython_pure_import_error = exc
else:
    cython_pure_import_error = None

try:
    from fibonacci_cython import fibonacci_cython
except ImportError as exc:
    fibonacci_cython = None
    cython_ext_import_error = exc
else:
    cython_ext_import_error = None


def benchmark_function(func, n, number):
    timer = timeit.Timer(lambda: func(n))
    total = timer.timeit(number=number)
    return total / number, total


def run_benchmarks():
    cases = [10, 20, 30, 40, 50, 100, 1000]
    common_number = 20000

    print("Benchmarking fibonacci implementations")
    print("Note: build Cython extensions first with `python setup.py build_ext --inplace` if needed.")
    print()

    if cython_pure_fibonacci is None:
        print("Warning: failed to import fibonacci_pure extension module:")
        print(cython_pure_import_error)
        print("Skipping fibonacci_pure benchmarks.\n")

    if fibonacci_cython is None:
        print("Warning: failed to import fibonacci_cython extension module:")
        print(cython_ext_import_error)
        print("Skipping fibonacci_cython benchmarks.\n")

    implementations = [
        ("pure Python", py_fibonacci),
    ]
    if cython_pure_fibonacci is not None:
        implementations.append(("cythonized py module", cython_pure_fibonacci))
    if fibonacci_cython is not None:
        implementations.append(("Cython extension", fibonacci_cython))

    for n in cases:
        print(f"n = {n}")
        for name, func in implementations:
            number = common_number
            if n >= 50:
                number = 2000
            elif n >= 100:
                number = 500

            avg, total = benchmark_function(func, n, number)
            print(f"  {name:20s}: {avg:.8f} sec/call (x{number}) total={total:.4f}s")
        print()


if __name__ == "__main__":
    run_benchmarks()
