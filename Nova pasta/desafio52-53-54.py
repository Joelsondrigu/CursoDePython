"""
pa = int(input('Digite o valor da PA: '))
pro = int(input('Digite a progressão: '))
for c in range(0,pa,pro):

    print(c)

n = int(input('Digite um numero: '))
if n % 3 == 0:
    print('O numero {} é primo'.format(n))
else:
    print('O numero {} não é primo'.format(n))
"""
totp = 0
totn = 0
n = int(input('Digite um numero: '))
for c in range(1,15):
    if n % c == 0:
        totp += 1
        print(c,'{} é primo'.format(n))
    else:
        totn += 1
        print(c,'{} não é primo'.format(n))
print('fim')
print('A Quantidade de numero primos é {}'.format(totp))
print('A Quantidade de numero Não primos é {}'.format(totn))















