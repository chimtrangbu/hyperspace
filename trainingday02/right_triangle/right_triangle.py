def right_triangle(a, b, c):
    if (b > a):
        a, b = b, a
    if (c > a):
        a, c = c, a
    if a * a == b * b + c * c:
        return True
    return False
