from scipy.integrate import simpson
import numpy as np

def simpson_integrate(f, a, b, n):
    """
    Calculates the definite integral of f(x) over [a, b] using Simpson's rule with n intervals.
    """
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return simpson(y, x)