def duplicare(n,d = 0):
    p = 1
    while(n != 0):
        if n % 10 % 2 != 0:
            d = (n % 10) * p + d
            p *= 10
            d = (n % 10) * p + d
        else:
            d = (n % 10) * p + d
        n = int(n/10)
        p *= 10
    return d

print(duplicare(2019, 0))