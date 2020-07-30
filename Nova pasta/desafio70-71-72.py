'''totH = tot18 = tot20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        totH += 1
    if idade >= 18:
        tot18 += 1
    if idade < 20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'O total de pessoas com mais de 18 anos é de: {tot18} pessoas')
print(f'O Total de homens cadastrados foi de: {totH} Homens ')
print(f'O total de mulheres com menos de 20 anos é de: {tot20} Mulheres')

n = int(input('Digite um numero: '))
for c in range(1,10):
    print(f'{n} x {c} = {n * c}')
n = int(input('Digite um numero: '))
print('Fim da Tabuada.')

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    for c in range(1,10):
        print(f'{n} x {c} = {n * c}')
print('Fim')

print('{:=^40}'.format(' LOJAS RODRIGUES '))
totP = tot1000 = totC = menor = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    totP += 1
    totC += preco
    if preco > 1000:
        tot1000 += 1
    if totP == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:=^40}'.format('Boas Compras'))
print(f'vc comprou {totP} produtos e total de suas compras foi de R$ {totC:.2f} Reais')
print(f'Temos {tot1000} produtos com valor acima de R$ 1000 Reais')
print(f'O {barato} foi o produto com menor valor de suas compras R$ {menor:.2f} Reais')
print('='*30)
print('{:^30}'.format('Banco GOLD'))
print('='*30)
saque = int(input('Digite o valor do saque:R$ '))
total = saque
cedula = 50
totced = 0
while True:
    if total >= cedula:
        total -= 50
        totced += 1
    else:
        print(f'O total de {totced} cédulas de R$ {cedula} Reais')
        if total >= 50:
            cedula = 20
            total -= 20
            totced += 1
        elif total >= 10:
            cedula = 10
            total -= 10
            totced += 1
        elif total >= 1:
            cedula = 1
            totced -= 1
            cedula = 0
        if total == 0:
            break
print(f'{totced} x {cedula} = R$ {totced * cedula:.2f}')
print('{:-^30}'.format(' Conte sempre conósco '))'''

print('='*30)
print('{:^30}'.format(' TABUADA '))
print('='*30)
while True:
    n = int(input('Digite um numero: '))
    if n == 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('{:^30}'.format('FIM DA TABAUADA'))







































