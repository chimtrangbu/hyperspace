def right_triangle_errors(a, b, c):
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(b, int)):
        raise ValueError('Incorrect value')
    elif (a <= 0 or b <= 0 or c <= 0):
        raise ValueError('Incorrect value')
    else:
        if (b > a):
            a, b = b, a
        if (c > a):
            a, c = c, a
        if a * a == b * b + c * c:
            return True
        return False
