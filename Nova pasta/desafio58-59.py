
"""
from random import randint
computador = randint(0,10)
print('Sou seu computador...acabei de pensar em um numero entre 0 e 10')
print('Será que vc consegue acertar? tente...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente.')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print('Parabéns vc acertou!!! com {} tentativas '.format(palpites))

print('======= MENU DE OPÇÕES =======')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:"""


print('======= MENU DE OPÇÕES 2 =======')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print("""[1] somar 
[2] multiplicar 
[3] maior 
[4] novos numeros 
[5] sair do programa """)
opcao = int(input('Qual é a sua opção? '))
if opcao == 1:
    soma = n1 + n2
    print('A soma é {}'.format(soma))
elif opcao == 2:
    mult = n1 * n2
    print('A multiplicação é {} '.format(mult))
elif opcao == 3:
    if n1 > n2:
        maior = n1
    elif n2 > n1:
        maior = n2
    print('O maior é: {} '.format(maior))
elif n1 == n2:
    print('O numeros são iguais')
elif opcao == 4:
    n3 = int(input('Digite um novo numero: '))
    n4 = int(input('Digite outro numero: '))
    print('Os novo numeros são: {} e {} '.format(n3, n4))
elif opcao == 5:
    print('fim')




















