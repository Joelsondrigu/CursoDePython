"""
nome = str(input('Qual é seu nome?'))
print('Silva' in nome)

n = str(input('Verificando nome, por favor digite: '))
print('SILVA' in n.upper())
"""
from random import randint
from time import sleep
pc = randint(0,5)
print('Eu já pensei no meu numero. E vc?')
humano = int(input('Vou digitar meu numero: '))
print('Processando...')
sleep(4)
if pc == humano:
    print('E ganhei de VC!! PC!!! meu numero foi: {}'.format(humano))
else:
    print('Eu é que ganhei!! Humano: meu numero foi {}' .format(pc))