"""
coposto = float(input('Digite o cateto oposto: '))
cadj = float(input("digite o cateto adjacente: "))
hipotenusa = (coposto ** 2 + cadj ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

import random
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
"""

from random import choice
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('terceiro aluno: '))
a4 = str(input('quarto aluno: '))
lista = [a1,a2,a3,a4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
