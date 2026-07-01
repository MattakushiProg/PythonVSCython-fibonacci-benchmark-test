# PythonVSCython-fibonacci-benchmark-test

This repository compares the performance of Fibonacci implementations in:
- pure Python (`fib.py`)
- Cython-annotated Python compiled as an extension module (`fib_pure.py`)
- a dedicated Cython `.pyx` extension (`fib_cython.pyx`)

## Requirements

- Python 3.x
- Cython
- setuptools

Install dependencies:

```bash
pip install -r requirements.txt
```

## Build

Build the Cython extension modules in-place:

```bash
python setup.py build_ext --inplace
```

This generates the compiled modules:
- `fibonacci_pure.cp*.pyd`
- `fibonacci_cython.cp*.pyd`

## Run the benchmark

Use `benchmark_fib.py` to compare speed across implementations:

```bash
python benchmark_fib.py
```

The script will:
- import the pure Python implementation from `fib.py`
- import the compiled Cython modules if available
- benchmark each implementation for several values of `n`
- print average time per call and total runtime

## Run the example

Run `main.py` to print Fibonacci results from both compiled modules:

```bash
python main.py
```

## Files

- `fib.py` - pure Python Fibonacci implementation
- `fib_pure.py` - Python function with Cython typing and compilation support
- `fib_cython.pyx` - native Cython extension implementation
- `benchmark_fib.py` - benchmarking script for all available implementations
- `main.py` - simple usage example importing the compiled modules
- `setup.py` - build configuration for Cython extension modules
- `requirements.txt` - dependency list

## Notes

- If import errors appear, ensure the extensions are built in the same directory as the script.
- Use a Python virtual environment to keep dependencies isolated.

