# File: tests/test_trapezoidal.py
import numpy as np
from sympy import symbols
from src.integration.trapezoidal import trapezoidal_numpy, trapezoidal_scipy, symbolic_integration

def test_trapezoidal_numpy_x2():
    f = lambda x: x**2
    result = trapezoidal_numpy(f, 0, 1, 100)
    assert abs(result - 1/3) < 1e-3

def test_trapezoidal_scipy_x2():
    f = lambda x: x**2
    result = trapezoidal_scipy(f, 0, 1, 100)
    assert abs(result - 1/3) < 1e-3

def test_symbolic_integration_x2():
    x = symbols('x')
    result = symbolic_integration(x**2, 0, 1)
    assert abs(float(result) - 1/3) < 1e-3