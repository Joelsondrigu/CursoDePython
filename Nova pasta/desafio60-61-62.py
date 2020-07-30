
"""from math import factorial
n = int(input('Entre com o numero para calcular o fatorial: '))
f = factorial(n)
print('O fatorial de {} é {} '.format(n,f))"""

n = int(input('Informe um numero para o cálculo do fatorial: '))
f = 1
c = n
while c > 0:
    f = f * c
    print('{} '.format(c),end='')
    print('x ' if c>1 else '=',end='')
    c -= 1
print(f)
