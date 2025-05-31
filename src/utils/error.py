def validate_parameters(a, b, n):
    """
    Validates the integration limits and the number of intervals.
    """
    if a >= b:
        raise ValueError("The lower limit (a) must be less than the upper limit (b).")
    if n <= 0 or n % 2 != 0:
        raise ValueError("The number of intervals (n) must be a positive even integer.")