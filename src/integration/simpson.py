from scipy.integrate import simpson
import numpy as np

def simpson_integrate(func, a, b, n):
    """
    Calculates the definite integral of func(x) over [a, b] using Simpson's rule with n intervals.
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
    if n % 2 != 0:
        raise ValueError("Simpson's rule requires an even number of intervals (n must be even).")

    x = np.linspace(a, b, n + 1)
    y = func(x)
    return simpson(y, x)