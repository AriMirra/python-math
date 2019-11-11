import math
import numpy as np

"""
@param y_list: y, y', y'', ..., y^k --> taylor of order k.
@param a     : interval initial value.
@param b     : interval end value.
@param h     : step.
@param x0    : x initial value.
@param y0    : y initial value.
"""
def taylor_integration(y_list, a, b, h, x0, y0):
    print("initial values: x0: " + str(x0) + ", y0: " + str(y0))
    y_previous = y0
    
    for xi in np.arange(a, b, h):
        line = "                x" + str(int(i)) + ": " + str(xi) + ", y" + str(int(i)) + ": "
        y_value = float(y_previous)
        i = 1
        for f in y_list:
            # hh = ((h / math.factorial(i)))
            # ii = f(xi)
            # value = ((h / math.factorial(i)) * f(xi))
            # print("                         h/factorial: " + str(hh) + ", y: " + str(ii) + ", value" + str(value))
            y_value += ((h / math.factorial(i)) * f(xi))
            i += 1
        line += str(y_value)
        print(line)
        y_previous = y_value
    print("finished")


if __name__ == "__main__":
    # example 1: practica 6 ejercicio 3
    y_i = lambda x: math.exp((-x) ** 2)
    y_ii = lambda x: -2 * x * math.exp((-x) ** 2)
    y_iii = lambda x: math.exp((-x) ** 2) * (-2 + 4 * (x ** 2))
    y_iv = lambda x: math.exp((-x) ** 2) * (8*x + 4*x - 8 * (x ** 3))
    a = 0.0
    b = 2.0
    h = 0.2
    x0 = 0.0
    y0 = 0.0
    taylor_integration([y_i, y_ii, y_iii, y_iv], a, b, h, x0, y0)
    