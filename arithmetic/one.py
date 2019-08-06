import math
from prettytable import PrettyTable


def calc_e(n_range):
    t = PrettyTable(['n', 'e', 'error'])
    for n in n_range:
        e = (1 + 1/n) ** n
        error = abs(e - math.e)
        t.add_row([n, e, error])
    print(t)


calc_e([10**x for x in range(2, 26)])
print('\n\n\n')
calc_e([x * 10**5 for x in range(160, 171)])
print('\n\n\n')
calc_e([x for x in range(16777200, 16777251)])

