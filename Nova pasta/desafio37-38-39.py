"""
num = int(input('Digite um numero inteiro: '))
print('ECOLHA UMA DAS OPÇÕES ABAIXO PARA CONVERSÃO:')
print('(1) para BINÁRIOS')
print('(2) para OCTAL')
print('(3) HEXADECIMAL')
opcao = int(input('Digite sua ecolha: '))
if opcao == 1:
    print('VC escolheu fazer a conversão para BINÁRIOS. {} em BINÁRIO É: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('VC escolheu fazer a conversão para OCTAL. {} em OCTAL É: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('VC escolheu fazer a conversão para HEXADECIMAL. {} em HEXADECIMAL É {}'.format(num, hex(num)[2:]))
else:
    print('[ERRO] Verifique o numero e tente novamente...')


numero = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))
if numero > numero2:
    print('O PRIMEIRO valor é maior')
elif numero2 > numero:
    print('O SEGUNDO valor é maior')
else:
    print('OS DOIS SÃO IGUAIS')
"""
from datetime import date
ano = date.today().year
ano_nasc = int(input('Digite o ano de seu nascimento: '))
idade = ano - ano_nasc
print('VC nasceu em {} e tem {} anos de idade.'.format(ano_nasc,idade))
if idade == 18:
    print('VC tem {} de idade e precisa se alistar imediatamente ao serviço militar.'.format(idade,))
elif idade < 18:
    saldo = 18 - idade
    alist = ano + saldo
    print('Vc tem {} anos e ainda faltam {} anos para vc se alistar'.format(idade,saldo))
    print('Seu alistamente vai ser no ano de {}'.format(alist))
elif idade > 18:
    saldo = idade - 18
    alist = ano - saldo
    print('Vc tem {} anos e ja passou {} anos de seu alistamento.'.format(idade,saldo))
    print('O Ano de seu alistamento foi em {}'.format(alist))























