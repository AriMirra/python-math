def spigot_pi(n):
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while n>0:
        p, q, k = k*k, 2*k+1, k+1
        a, b, a1, b1 = a1, b1, p*a+q*a1, p*b+q*b1
        d, d1 = a/b, a1/b1
        while d == d1:
            yield int(d)
            n -= 1
            a, a1 = 10*(a%b), 10*(a1%b1)
            d, d1 = a/b, a1/b1

print(str(eval(''.join(str(e) for e in list(spigot_pi(3)))) * (10**-2)))
print(str(eval(''.join(str(e) for e in list(spigot_pi(10)))) * (10**-10)))
print(str(eval(''.join(str(e) for e in list(spigot_pi(20)))) * (10**-19)))
