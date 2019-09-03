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


def s(i, cs, xs):
    s = 0
    for j in range(i):
        p = 1
        for k in range(j):
            p *= xs[i] - xs[k]
        s += cs[j] * p

    return s


def q(i, xs):
    p = 1
    for k in range(i):
        p *= xs[i] - xs[k]
    return p


def newton_pol(xs, ys):
    cs = []
    n = len(xs)
    for i in range(n):
        ck = (ys[i] - s(i, cs, xs)) / q(i, xs)
        cs.append(ck)
    print(cs)
    pol_str = ""
    for i in range(n):
        pol_str += str(cs[i])
        for j in range(i):
            pol_str += "*(x-%s)" % xs[j]
        if i != n - 1:
            pol_str += " + "
    return lambda x: eval(pol_str, {'x': xs})


print(newton_pol([1.5, 1, 0.5, 2], [1, 0.5, 1.2, 3]))
