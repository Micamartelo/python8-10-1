n = int(input('Fatorial de:'))
c = n
f = 1
print('Calculando {}! = '.format(n))
while c > 0:
    print('{}'.format(c))
    print('x' if c>1 else '=')
    f *= c
    c -= 1
print('{}'.format(f))