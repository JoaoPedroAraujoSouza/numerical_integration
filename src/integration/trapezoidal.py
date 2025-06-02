import numpy as np
from scipy.integrate import trapezoid

def trapezoidal_integrate(func, a, b, n):
    """
    Calculates the definite integral of func(x) over [a, b] using the trapezoidal rule with n intervals.
    """
    if not callable(func):
        raise ValueError("Parameter 'func' must be a function.")
    if not isinstance(a, (int, float)):
        raise TypeError("Lower limit 'a' must be a number.")
    if not isinstance(b, (int, float)):
        raise TypeError("Upper limit 'b' must be a number.")
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of intervals 'n' must be a positive integer.")
    if a >= b:
        raise ValueError("Lower limit 'a' must be less than upper limit 'b'.")

    x = np.linspace(a, b, n + 1)
    y = func(x)
    return trapezoid(y, x)