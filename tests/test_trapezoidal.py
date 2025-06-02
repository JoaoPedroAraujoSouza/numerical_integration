from src.integration.trapezoidal import trapezoidal_integrate

def test_trapezoidal_integrate_x2():
    f = lambda x: x**2
    result = trapezoidal_integrate(f, 0, 1, 100)
    assert abs(result - 1/3) < 1e-3

def test_trapezoidal_invalid_func():
    try:
        trapezoidal_integrate(123, 0, 1, 10)
        assert False
    except ValueError:
        assert True