#50
"""
n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))
n4 = int(input('Digite um numero:'))
n5 = int(input('Digite um numero:'))
n6 = int(input('Digite um numero:'))
soma = 0
if n1 % 2 == 0:
    soma = soma + n1
if n2 % 2 == 0:
    soma = soma + n2
if n3 % 2 == 0:
    soma = soma + n3
if n4 % 2 == 0:
    soma = soma + n4
if n5 % 2 == 0:
    soma = soma + n5
if n6 % 2 == 0:
    soma = soma + n6
print('A soma é',soma)
print('fim')



#51 NR


#52
n = int(input('Digite um numero: '))
if n % 3 == 0:
    print('É um numero primo.')
else:
    print('Não é um numero primo.')

#53 NR

#frase = str(input('Digite uma frase: '))

#54
from datetime import date
ano = date.today().year
maior = 0
menor = 0
m = 21
n1 = int(input('Digite seu ano de nascimento: '))
n2 = int(input('Digite seu ano de nascimento: '))
n3 = int(input('Digite seu ano de nascimento: '))
n4 = int(input('Digite seu ano de nascimento: '))
n5 = int(input('Digite seu ano de nascimento: '))
n6 = int(input('Digite seu ano de nascimento: '))
n7 = int(input('Digite seu ano de nascimento: '))
for c in range(1,8):
    if (ano - n1) >= m:
        maior = + 1
    else:
        menor = + 1

print('O numero de menores é ',menor)
print('O numero de maiores é ',maior)

count = 0
soma = 0
for c in range(1,7):
    num = int(input('Digite {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print('Você informou {} numeros PARES e a soma foi {}'.format(count,soma))

"""
soma = 0
count = 0
for c in range(1,7):
    num = int(input('Digite o {} numero: '.format(c)))
    if num % 2 == 0:
        soma += num
    count += 1
print('VC digitou {} numeros e a soma é de {}'.format(count,soma))







