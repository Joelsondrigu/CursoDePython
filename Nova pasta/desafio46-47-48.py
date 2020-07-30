
from time import sleep
for c in range(10, 0, -1):
    print('Falta: ',c)
    sleep(1)
print('FOGOS!!!! \O/\o/\O/')


from time import sleep
n = int(input('Digite o tempo para iniciar contagem regressíva: '))
for c in range(n,0,-1):
    print(c)
    sleep(2)
print('FOGOS!!!! \O/\o/\O/')


from time import sleep
tempo = int(input("DIGITE A CONTAGEM REGRESSÍVA: "))
for tempo in range(tempo,0,-1):
    print(tempo)
    sleep(1)
print('FOGOS!!!! \O/\o/\O/....FOGOS!!!! \O/\o/\O/...FOGOS!!!! \O/\o/\O/')


from time import sleep
n = int(input('Tempo para contagem regressíva: '))
for n in range(n,0,-1):
    print(n)
    sleep(1)
print('FOGOS!!!! \O/\o/\O/....FOGOS!!!! \O/\o/\O/...FOGOS!!!! \O/\o/\O/')


from time import sleep
n = int(input('Digite a contagem regressiva: '))
for c in range(n,0,-1):
    print(c)
    sleep(1)
print('FOGOS!!!! \O/\o/\O/....FOGOS!!!! \O/\o/\O/...FOGOS!!!! \O/\o/\O/')


#47
for c in range(1,50, ):
    if c % 2 == 0:
        print('numero par',c)
print('fim')

for c in range(2,50,2):
    print('numero par',c)
print('fim')


#48
soma = 0
for n in range(3,500,2):
    if n % 3 == 0:
        soma = soma + n
        print('Numero ímpar',n)
print(soma)
print('Fim')


#49
mult = 0
print('========= TABUADA ========')
n = int(input('Digite um numero: '))
for contador in range(1,21):
    mult = n * contador
    print(n,'x',contador,'=',mult)


mult = 0
n = int(input('Digite um numero: '))
for c in range(1,31):
    mult = n * c
    print(n,'x',c,'=',mult)


print('======= TABUADA =======')
soma = 0
n = int(input('Digite um numero: '))
for c in range(1,11):
    soma = n + c
    print(n,'+',c,'=',soma)


print('=======> TABUADA <=======')
sub = 0
n = int(input('Digite um numero: '))
for c in range(1,10):
    sub = n - c
    print(n,'-',c,'=',sub)


print('======= TABUADA =======')
d = 0
n = int(input('Digite um numero: '))
for c in range(1,10):
    d = n / c
    print(n,'/',c,'=',d)


















