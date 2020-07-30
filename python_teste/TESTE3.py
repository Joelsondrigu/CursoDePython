c = 1
while c<= 10:
    print(c,' ',end='')
    c += 2
print('Fim')
n = 0
while n != 999:
    n = int(input('Digite um numero: '))
print('Fim')

c = 0
while c < 5:
    n = int(input('Digite um numero: '))
    c += 1
print('fim')

n = s = 0
while n != 999:
    n = int(input('Digite um numero: '))
    s += n
s = s - 999
print('A soma é de {} '.format(s))

c = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print(f'VC digitou {c} e a soma do total e de {s} ')

nome = 'JR'
idade = 29
print('O {} tem {} anos de idade.'.format(nome,idade))
print(f'O {nome} tem {idade} anos de idade.')
print('O',nome,'tem',idade,'anos de idade.')

nome = 'JR'
idade = 25
salario = 4000.00
print('O {} tem {} anos de idade e seu salario é de R$ {:.2f} '.format(nome,idade,salario))
print(f'O {nome:=^20} tem {idade} anos de idade e seu salario é de R$ {salario:.2f} ')

n = int(input('Informe um numero: '))
for c in range(1,10):
    print(f'{n} x {c} = {n * c}')
    n = int(input('Informe um numero: '))
print('fim')
i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i,f,p):
    print(f'{c}')


i = int(input('Digite o início: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for c in range(i,f,-p):
    print(f'{c}')
n = int(input('Digite um numero: '))
c = n
while c < 10:
    print(f'{n} x {c} = {n*c}')
    c += 1
print('fim')


conta = s = 0
n = 1
while n != 0:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s = s + n
    conta += 1
print(f'{conta} {s}')
print('fim')





































