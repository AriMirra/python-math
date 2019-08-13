

def bisection(f, a, b, error_level=0.001):
    previous_p = a
    error = error_level + 1
    while error < error_level:
        p = (a + b) / 2
        error = abs(p - previous_p)
        previous_p = p
        if f(a) * f(p) > 0:
            a = p
        elif f(b) * f(p) < 0:
            b = p
        else:
            return p
        return p


