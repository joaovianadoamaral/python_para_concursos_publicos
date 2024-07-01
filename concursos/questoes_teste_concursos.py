def func(n):
    if n == 0:
        return[]
    return [n] + func(n-1) + [n]
n = int(input('Valor de n positivo: '))
seq = func(n)
print(' '.join(map(str,seq)))
