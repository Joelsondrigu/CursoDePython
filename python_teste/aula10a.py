"""
nome = str(input('Qual é seu nome? '))
if nome == 'Joelson':
    print('Seu nome é muito bonito! ')
print('Bom dia, {}!'.format(nome))

nome = str(input('Qual é seu nome? '))
if nome == 'Joelson':
    print('Seu nome é muito bonito!')
else:
    print('Seu nome é tão normal...')
print('Bom dia, {}!'.format(nome))
"""

n1 = float(input('Digite a sua nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media >= 6.0:
    print('Parabéns! vc foi aprovado! sua média foi: {:.1f}'.format(media))
else:
    print('OPs! vc não foi aprovado! sua média foi: {:.1f}'.format(media))