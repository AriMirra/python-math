def double_range_generator(n):
    for i in range(1, n + 1):
        yield i * 2

print(list(double_range_generator(3)))