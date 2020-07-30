"""
print('==========IMC==========')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu IMC é {:.2f} e seu peso está ABAIXO DO PESO IDEAL com {} kg'.format(imc,peso))
elif imc <= 25:
    print('Seu IMC é de {:.2f} e vc ESTÁ NO SEU PESO IDEAL com {} kg'.format(imc,peso))
elif imc <= 30:
    print('Seu IMC é de {:.2f} e vc está com SOBREPESO com {} kg'.format(imc,peso))
elif imc <= 40:
    print('Seu IMC é de {:.2f} e vc está com OBESIDADE com {} kg'.format(imc,peso))
else :
    print('ATENÇÃO: seu IMC é de {:.2f} e vc está com obesidade mórbida com {} kg'.format(imc,peso))

print("{:=^40}".format(' LOJAS RODRIGUES '))
vprod = float(input('Qual o valor do produto? R$ '))
print('ESCOLHA A FORMA DE PAGAMENTO: ')
print('[1]À VISTA NO DINHEIRO/CHEQUE:')
print('[2]À VISTA NO CARTÃO DE CREDITO:')
print('[3]PARCELADO NO CARTÃO DE CRÉDITO:')
formapg = int(input('ESCOLHA A FORMA DE PAGAMENTO: '))

if formapg == 1:
    valorpg = vprod - (vprod*10/100)
    print('OK! VC pagou {:.2f} Reais e ganhou 10% DE DESCONTO'.format(valorpg))
    print('OBRIGADO E VOLTE SEMPRE!')
elif formapg == 2:
    valorpg = vprod - (vprod*5/100)
    print('OK! VC pagou {:.2f} Reais à vista no seu cartão e ganhou 5% de DESCONTO'.format(valorpg))
    print('OBRIGADO E VOLTE SEMPRE!')
elif formapg == 3:
    parc = float(input('Em quantas vezes deseja parcelar? '))
    if parc == 2:
        valorpg = vprod
        parcela = (vprod / 2)
        print('OK! vc pagou {:.2f} em 2 x parcelas de {:.2f} sem juros no cartão'.format(valorpg,parcela))
    elif parc == 3:
        valorpg = vprod + (vprod*20/100)
        parcela = (valorpg/ 3)

        print('OK! valor do produto {:.2f} vc pagou {:.2f} em \n 3 x parcelas de {:.2f} com juros de 20% no cartão'.format(vprod,valorpg, parcela))
"""

from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('suas opções:')
print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')
jogador = int(input('Qua é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*12)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*12)

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
            print('JOGADOR VENCE!')
    elif jogador == 1:
            print('COMPUTADOR VENCE!')
    elif jogador == 2:
            print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')



















































