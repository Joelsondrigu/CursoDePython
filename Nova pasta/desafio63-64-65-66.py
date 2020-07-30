'''c = 's'
soma = 0
media = 0
conta = 0
while c != 'n':
    n = int(input('Digite um numero: '))
    soma += n
    conta += 1
    c = str(input('Deseja continuar? [S/N] '))
media = (soma/conta)
print('contados {} a soma é {} a media é {} '.format(conta,soma,media))

c = 's'
soma = media = conta = maior = menor = 0
while c != 'n':
    n = int(input('Digite um numero: '))
    soma += n
    conta += 1
    if conta == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Deseja continuar? [S/N] '))
media = (soma/conta)
print('contados {} a soma é {} a media é {} o maior é {} e o menor é {}'.format(conta,soma,media,maior,menor))'''


c = 's'
soma = count = media = maior = menor = 0
while c != 'n':
    n = int(input('Digite um numero: '))
    soma = soma + n
    count = count + 1
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Deseja continuar? S/N '))
media = soma/count
print('contado',count,'somado',soma,'media',media,'menor é: ',menor,'maior é',maior)

















