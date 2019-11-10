from trapezius import *
import math


def two_a():
    f = lambda x: 1 / (1 + x)
    a = 0
    b = 1
    h = 0.5
    print(trapezius(f, a, b, h))

def two_b():
    f = lambda x: 1 / (1 + x)
    a = 0
    b = 1
    h = 0.5
    print(trapezius(f, a, b, h))
    print()

def three_a():
    f = lambda x: math.sin(x) / x
    a = 2
    b = 3
    h = 0.1
    print(trapezius(f, a, b, h))

def three_b():
    f = lambda x: 4 / (math.pi * (1 + x ** 2))
    a = 0
    b = 1
    h = 0.2
    print(trapezius(f, a, b, h))

def three_c():
    f1 = lambda x: math.sin(x) / x
    f1_second_der = lambda x: - (math.sin((x ** 2) - 2) + math.cos((x ** 2) + x)) / (x ** 3)
    a1 = 2
    b1 = 3
    h1 = 0.1
    print(trapezius_error(f1, f1_second_der, a1, b1, h1))

    f2 = lambda x: 4 / (math.pi * (1 + x ** 2))
    f2_second_der = lambda x: - (8 * (-3*(x**2) + 1)) / (math.pi * (1 + x**2)**3) 
    a2 = 0
    b2 = 1
    h2 = 0.2
    print(trapezius_error(f2, f2_second_der, a2, b2, h2))


if __name__ == "__main__":
    print("3 a\n---------------------")
    three_a()
    print("\n\n3 b\n---------------------")
    three_b()
    print("\n\n3 c\n---------------------")
    three_c()