class Interval:
    """Represents closed intervals on the number line.

    Attributes:
    a -- the left end of the interval
    b -- the right end of the interval

    Example:
    >>> A = Interval(-20, 200)
    >>> B = Interval(10, 10)
    >>> C = Interval(30, 4)
    >>> repr(A)
    'Interval(-20, 200)'
    >>> 120 in A
    True
    >>> 200 in A
    True
    >>> -20 in A
    True
    >>> 201 not in A
    True
    >>> -50 not in A
    True
    >>> 10 in B
    True
    >>> 11 not in B
    True
    >>> 10 not in C
    True
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Interval({self.a}, {self.b})"

    def __contains__(self, x):
        return self.a <= x <= self.b


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)