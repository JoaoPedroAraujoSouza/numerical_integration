from src.integration.simpson import simpson_integrate

def test_simpson_integrate_x2():
    f = lambda x: x**2
    result = simpson_integrate(f, 0, 1, 10)
    assert abs(result - 1/3) < 1e-3

def test_simpson_invalid_func():
    try:
        simpson_integrate(123, 0, 1, 10)
        assert False
    except ValueError:
        assert True