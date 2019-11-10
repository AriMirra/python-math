import types
import numpy as np
import math

"""
Trapezius Rule (an approximation of an integral)
@param f: lambda function, f(i) returns a float value.
@param a: interval initial x value, float. 
@param b: interval final x value, float.
@param h: interval step, float.
@return : float (area).
"""
def trapezius(f, a, b, h):
    # print("a: " + str(a) + ", b: " + str(b) + ", h: " + str(h)) 
    if f is None or a is None or b is None or h is None:
        raise ValueError("f, a, b or h is None")
    if type(f) is not types.LambdaType:
        raise TypeError("f is not a lambda function")
    result = 0
    for i in np.arange(a, b, h):
        if i is a or b:
            value = f(i)
            # print("value is: " + str(value))
            result += value
        else:
            value = f(i)
            # print("value is: " + str(value))
            result += 2 * value
    # print("last: " + str(float((b-a) / 2)))
    result *= ((b - a) / 2)
    return result


def trapezius_error(f, f_second_der, a, b, h):
    first  = ((b - a) / 12) * (h ** 2) * f_second_der(a)
    second = ((b - a) / 12) * (h ** 2) * f_second_der(b)
    if first > second:
        return first
    else:
        return second


if __name__ == "__main__":
    f = lambda x: math.sin(x) / x
    a = 2
    b = 3
    h = 0.1
    print(trapezius(f, a, b, h))