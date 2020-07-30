"""
def minha_funcao(numero):
    if numero % 2 == 0:
        return '{} é par'.format(numero)
    else:
        return '{} é ímpar'.format(numero)
    return "zero é neutro"

resultado = minha_funcao(0)
"""
print('{:=^30}'.format(' LOJAS RODRIGUES '))
valorpg = float(input('Entre com o valor das compras: '))
print('[1] À VISTA NO DINHEIRO/CHEQUE')
print('[2] À VISTA NO CARTÃO DE CRÉDITO')
print('[3] PARCELADO NO CARTÃO DE CRÉDITO')
formapg = float(input('ESCOLHA a forma de pagamento: '))
if formapg == 1:
    totalpg = valorpg - (valorpg * 10/100)
    print('{:=^30}'.format(' LOJAS RODRIGUES '))
    print('O valor da compra é de R$ {:.2f} e vc ganhou 10% de desconto por ter pago à vista'.format(valorpg))
    print('Com o desconto vc vai pagar o valor de R$ {:.2f} Reais'.format(totalpg))
    print('OBRIGADO E VOLTE SEMPRE!')
elif formapg == 2:
    totalpg = valorpg - (valorpg * 5/100)
    print('{:=^30}'.format(' LOJAS RODRIGUES '))
    print('O valor de sua compra é de R$ {:.2f} e vc ganhou 5% de desconto por ter pago à vista no cartão'.format(valorpg))
    print('Com o desconto vc vai pagar o valor de R$ {:.2f} Reais'.format(totalpg))
    print('==OBRIGADO E VOLTE SEMPRE!==')
elif formapg == 3:
    parc = int(input('Quantas parcelas deseja fazer? '))
    if parc == 2:
        totalpg = valorpg
        parcelado = valorpg / 2
        print('O valor de suas compras é de R$ {:.2f} Reais e vc optou por pagar em 2x no cartão'.format(totalpg))
        print('O valor ficará em 2x de R$ {:.2f} Reais somando o total de R$ {:.2f}'.format(parcelado,totalpg))
        print('==OBRIGADO E VOLTE SEMPRE!==')
    if parc == 3:
        totalpg = valorpg + (valorpg * 20/100)
        parcelado = totalpg / 3
        print('O valor de suas compras é de R$ {:.2f} Reais e vc optou por pagar em 3x no cartão'.format(totalpg))
        print('O valor ficará em 3x de R$ {:.2f} Reais somando o total de R$ {:.2f} Reais com 20% de juros'.format(parcelado, totalpg))
        print('==OBRIGADO E VOLTE SEMPRE!==')
    else:
        print('[ERRO] verifique os dados e tente novamente!')















