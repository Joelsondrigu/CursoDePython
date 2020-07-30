"""
print('====SOFTWARE VENDA DE PASSAGEM====')
dtc = float(input('Digite a distância da sua viagem em km/h? '))
if dtc <= 200:
    preco = dtc * 0.50
    print('Sua viagem é de {} km e o valor é R$ {:.2f}'.format(dtc,preco))
else:
    preco = dtc * 0.45
    print('Sua viagem é de {} km e o valor é de R$ {:.2f}'.format(dtc,preco))
print('====OBRIGADO! e BOA VIAGEM!====')

from datetime import date
ano = int(input('Qual ano deseja analisar? '))
ano = date.today().year
if ano % 2 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano de {} não é BISSEXTO '.format(ano))

"""
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))
if a<b and a<c:
    print('O menor é {} q é a'.format(a))
if b<a and b<c:
    print('O menor é {} q é b '.format(b))
if c<a and c<b:
    print('O menor é {} q é C'.format(c))
