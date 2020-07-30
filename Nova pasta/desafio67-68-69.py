soma = n = c = 0
while n != 999:
    n = int(input('Digite um numero inteiro: '))
    c = c + 1
    soma += n
print('vc digitou {} numeros e a soma é de {} '.format(c - 1,soma -999))
n = 0
conta = 0
soma = 0
while n != 999:
    n = int(input('Digite um numero inteiro: '))
    conta += 1
    soma += n
tot = soma - 999
print('vc digitou {} numeros e a soma total e {}'.format(conta - 1,tot))
soma = 0
cont = 0
n = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Vc digitou {cont} numeros e a soma é {soma}')
soma = cont = n = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 0:
        break
    soma = soma + n
    cont = cont + 1
print(f'Vc digitou {cont} numeros e a soma é {soma}')
cont = soma = cont = n = 0
while n != 999:
    n = int(input('Digite um numero inteiro: '))
    cont += 1
    soma += n
total = soma - 999
contador = cont - 1
print(f'vc digitou {contador} é a soma é {total}')
s = c = 0
while True:
    n = int(input('Digite um numero inteiro: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'vc digitou {c} numeros e a soma é {s}')
print('======== MENU TABUADAS ========')
num = int(input('Digite um numero: '))
print('[1] ADIÇÃO')
print('[2] DIVISÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] SUBTRAÇÃO')
opcao = int(input('Escolha sua opção: '))
if opcao == 1:
        c = 0
        while c < 10:
            c += 1
            tab = c + num
            print(num,'+',c,'=',tab)
print('Fim')
num = int(input('Digite um numero: '))
print('[1] ADIÇÃO')
print('[2] DIVISÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] SUBTRAÇÃO')
opcao = int(input('Escolha sua opção: '))
if opcao == 2:
        c = 0
        while c < 10:
            c += 1
            tab = c / num
            print(num,'/',c,'=',tab)
print('Fim')
num = int(input('Digite um numero: '))
print('[1] ADIÇÃO')
print('[2] DIVISÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] SUBTRAÇÃO')
opcao = int(input('Escolha sua opção: '))
if opcao == 3:
        c = 0
        while c < 10:
            c += 1
            tab = c * num
            print(num,'x',c,'=',tab)
print('Fim')
num = int(input('Digite um numero: '))
print('[1] ADIÇÃO')
print('[2] DIVISÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] SUBTRAÇÃO')
opcao = int(input('Escolha sua opção: '))
if opcao == 4:
        c = 0
        while c < 10:
            c += 1
            tab = num - c
            print(num,'-',c,'=',tab)
print('Fim')

print('======== MENU TABUADAS ========')
num = int(input('Digite um numero: '))
print('[1] ADIÇÃO')
print('[2] DIVISÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] SUBTRAÇÃO')
opcao = int(input('Escolha sua opção: '))
if opcao == 1:
    c = 0
    while c < 10:
        c += 1
        tab = num + c
        print(num,'+',c,'=',tab)
elif opcao == 2:
    c = 0
    while c < 10:
        c += 1
        tab = num / c
        print(num, '/', c, '=', tab)
    print('fim')
elif opcao == 3:
    c = 0
    while c < 10:
        c += 1
        tab = num * c
        print(num, 'x', c, '=', tab)
    print('fim')
elif opcao == 4:
    c = 0
    while c < 10:
        c += 1
        tab = num - c
        print(num, '-', c, '=', tab)
    print('Fim')

while True:
    print('======== MENU TABUADA ========')
    num = int(input('Digite um numero: '))
    if num == -1:
        break
    for c in range(0,10):
        c += 1
        tab = num * c
        print(num,'x',c,'=',tab)
print('==== TABUADAS ENCERRADA ========')

while True:
    print('='*29)
    print('---------->TABUADA<----------')

    n = int(input('Digite um numero inteiro: '))
    if n < 0:
        break
    for c in range(0,10):
        c += 1
        tab = n + c
        print(f'{n} + {c} = {tab}')

while True:
    print('='*29)
    print('---------->TABUADA<----------')
    n = int(input('Digite um numero para ver a tabuada: '))
    if n == -1:
        break
    for c in range(0,10):
        c += 1
        tab = n - c
        print(f'{n} - {c} = {tab}')
print('Tabuada encerrada!')

while True:
    print('='*29)
    print('---------->TABUADA<----------')
    num = int(input('Digite um numero: '))
    if num < 0:
        break
    for c in range(0,10):
        c += 1
        tab = num/c
        print(f'{num} / {c} = {tab}')
print('Tabuada Encerrada!')


while True:
    print('='*29)
    num = int(input('Digite um numero inteiro: '))
    if num == -1:
        break
    for c in range(1,10):
        tab = num + c
        print('{} + {} = {}'.format(num,c,tab))
print('Fim da tabuada!')

while True:
    print('=' * 20)
    num = int(input('Digite um numero:'))
    if num == -1:
        break
    for c in range(1,10):
        print(f'{num} x {c} = {num*c}')
        c += 1
print('Fim da Tabuada!')

num = int(input('Digite um numero: '))
for c in range(1,10):
    print(f'{num} x {c} = {num*c}')
    c += 1
print('Fim da tabuada!')

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    for c in range(1,10):
        print(f'{n}x{c} = {n*c}')
        c += 1
print('Fim da Tabuada.')
soma = cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'vc digitou ao todo {cont} e a soma é {soma}',end='')
cont = 0
while True:
    from random import randint
    pc = randint(1,5)
    print('Sou seu PC e escolhi u numero agora escolha o seu: ')
    jogador = int(input('Digite um numero: '))
    if jogador == pc:

        print('Jogador ganhou!!')
        print(f'Vc ganhou mais o pc ganhou {cont} vezes')

        break
    else:
        print('O PC ganhou!!')
        cont += 1
garotasmenor = 0
mulherjoven = 0
mulheradulta = 0
homemjovem = 0
homemadulto = 0
mulher = 0
homem = 0
while True:
    sexo = str(input('Cadastro Informe seu sexo: '))
    if sexo == 'M':
        homem += 1
        idade = int(input('Casadtro Digite sua idade: '))
        if idade > 18:
            homemadulto += 1
        else:
            homemjovem += 1
    if sexo == 'F':
        mulher += 1
        idade = int(input('Casadtro Digite sua idade: '))
        if idade > 18:
            mulheradulta += 1
        else:
            mulherjoven += 1
            garotasmenor += 1

    c = str(input('Deseja Continuar: '))
    if c == 'n':
        break
print(f'maiores de 18 são {(homemadulto+mulheradulta)} total de homens cadastrados foi {homem} o total de mulheres com menos de 18 é  {mulherjoven}'
      f'e o total de pessoas cadastradas é de {homem+mulher}')
tot18 = tot20 = totH = totalP = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()[0]
    totalP += 1
    if idade > 18:
        tot18 += 1
    if idade < 20 and sexo == 'F':
        tot20 += 1
    if sexo == 'M':
        totH += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é de {tot18}.')
print(f'O total de mulheres com menos de 20 anos é de {tot20}.')
print(f'O total de Homens cadastrados foi de {totH}.')
print('O TOTAL de pessoas cadastradas foi de {}'.format(totalP))

tot18 = tot20 = totH = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if idade < 20 and sexo == 'F':
        tot20 += 1
    if sexo == 'M':
        totH += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'O total de pessoas com mais de 18 anos é de: {tot18}')
print(f'O total de mulheres com menos de 20 anos é de: {tot20}')
print('O Total de Homens cadastrados é de: {}'.format(totH))
























































































































































