"""num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[34m', end='')
        tot += 1
    else:
         print('\033[33m',end='')
    print('{}'.format(c),end=' ')
print('o numero {} foi divisivel por {} vezes '.format(c,tot))
if tot == 2:
    print('é primo')
else:
    print('Não é primo')

sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()[0]
if sexo == 'M' or sexo == 'm':
    sexo = 'Masculino'
elif sexo == 'F' or sexo == 'f':
    sexo = 'Feminino'
print('sexo {} registrado com sucessso!'.format(sexo))"""

sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite seu sexo: ')).strip()
if sexo == 'M' or sexo == 'm':
    sexo = 'Masculino'
elif sexo == 'F' or sexo == 'f':
    sexo = 'Feminino'
print('sexo {} registrado com sucesso '.format(sexo))




















