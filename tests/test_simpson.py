import numpy as np
from src.integration.simpson import simpson_integrate

def test_simpson_integrate_x2():
    f = lambda x: x**2
    result = simpson_integrate(f, 0, 1, 10)
    assert abs(result - 1/3) < 1e-3