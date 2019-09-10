import math
import matplotlib.pyplot as plt


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
    return lambda x: eval(pol_str, {'x': x})


def amplify(xs, ys, n):
    between_points = math.ceil((n - len(xs)) / (len(xs) - 1))
    new_xs = []
    new_ys = []
    for i in range(len(xs) - 1):
        delta = (xs[i + 1] - xs[i]) / (between_points + 1)
        temp_xs = [xs[i], xs[i + 1]]
        temp_ys = [ys[i], ys[i + 1]]
        temp_pol = newton_pol(temp_xs, temp_ys)
        for j in range(between_points + 1):
            new_x = xs[i] + j * delta
            new_y = temp_pol(new_x)
            new_xs.append(new_x)
            new_ys.append(new_y)
    new_xs.append(xs[len(xs) - 1])
    new_ys.append(ys[len(ys) - 1])
    return new_xs, new_ys


def simple_amplify(xs, n):
    between_points = math.ceil((n - len(xs)) / (len(xs) - 1))
    result = []
    for i in range(len(xs) - 1):
        delta = (xs[i + 1] - xs[i]) / (between_points + 1)
        for j in range(between_points + 1):
            result.append(xs[i] + j * delta)
    result.append(xs[len(xs) - 1])
    return result


xss = [1, 2, 3, 4, 5]
yss = [1, 4, 9, 16, 25]
new_xss, new_yss = amplify(xss, yss, 1000)

plt.plot(xss, yss)
plt.show()
plt.plot(new_xss, new_yss)
plt.show()
