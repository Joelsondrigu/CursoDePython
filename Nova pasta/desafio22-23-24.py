
nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('O seu nome tem {} letras '.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} '.format(nome.find(' ')))

n = int(input('Digite um numero: '))
un = str(n)
print('Analisando numero...')
print('Milhar é {}'.format(un[0]))
print('Centena é {} '.format(un[1]))
print('Dezena é {} '.format(un[2]))
print('Unidade é {} '.format(un[3]))

cid = str(input('Qual cidade vc nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

cidade = str(input('Digite a cidade que vc nasceu: ')).strip()
print(cidade[:2].upper() == 'SÃO PAULO')

