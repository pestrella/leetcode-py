def gcd(a, b):
    """
    Return the greatest common divisor of a and b
    """
    if b == 0:
        return a

    return gcd(b, a % b)
