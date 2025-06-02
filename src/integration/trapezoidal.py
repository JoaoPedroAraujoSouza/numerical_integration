import numpy as np
from scipy.integrate import trapezoid
from sympy import symbols, integrate, Basic

# Define the function
def f(x):
    return x**2

# Using numpy for manual trapezoidal method
def trapezoidal_numpy(func, a, b, n):
    try:
        if not callable(func):
            raise ValueError("O parâmetro 'func' deve ser uma função válida.")
        if not isinstance(a, (int, float)):
            raise TypeError("O limite inferior 'a' deve ser um número.")
        if not isinstance(b, (int, float)):
            raise TypeError("O limite superior 'b' deve ser um número.")
        if not isinstance(n, int) or n <= 0:
            raise ValueError("O número de subdivisões 'n' deve ser um inteiro positivo.")
        if a >= b:
            raise ValueError("O limite inferior 'a' deve ser menor que o limite superior 'b'.")

        x = np.linspace(a, b, n + 1)
        y = func(x)
        h = (b - a) / n
        return (h / 2) * (y[0] + 2 * sum(y[1:-1]) + y[-1])
    except Exception as e:
        print(f"Erro no método numpy: {e}")

# Using scipy for trapezoidal integration
def trapezoidal_scipy(func, a, b, n):
    try:
        if not callable(func):
            raise ValueError("O parâmetro 'func' deve ser uma função válida.")
        if not isinstance(a, (int, float)):
            raise TypeError("O limite inferior 'a' deve ser um número.")
        if not isinstance(b, (int, float)):
            raise TypeError("O limite superior 'b' deve ser um número.")
        if not isinstance(n, int) or n <= 0:
            raise ValueError("O número de subdivisões 'n' deve ser um inteiro positivo.")
        if a >= b:
            raise ValueError("O limite inferior 'a' deve ser menor que o limite superior 'b'.")

        x = np.linspace(a, b, n + 1)
        y = func(x)
        return trapezoid(y, x)
    except Exception as e:
        print(f"Erro no método scipy: {e}")

# Using sympy for symbolic integration
def symbolic_integration(func_expr, a, b):
    try:
        if not isinstance(func_expr, Basic):
            raise TypeError("O parâmetro 'func_expr' deve ser uma expressão simbólica válida.")
        if not isinstance(a, (int, float)):
            raise TypeError("O limite inferior 'a' deve ser um número.")
        if not isinstance(b, (int, float)):
            raise TypeError("O limite superior 'b' deve ser um número.")
        if a >= b:
            raise ValueError("O limite inferior 'a' deve ser menor que o limite superior 'b'.")

        x = symbols('x')
        return integrate(func_expr, (x, a, b))
    except Exception as e:
        print(f"Erro no método sympy: {e}")

# Parameters
a = 0
b = 1
n = 100

# Results
try:
    numpy_result = trapezoidal_numpy(f, a, b, n)
    print(f"Resultado usando numpy: {numpy_result}")

    scipy_result = trapezoidal_scipy(f, a, b, n)
    print(f"Resultado usando scipy: {scipy_result}")

    x = symbols('x')
    sympy_result = symbolic_integration(x**2, a, b)
    print(f"Resultado usando sympy: {sympy_result}")
except Exception as e:
    print(f"Erro geral: {e}")