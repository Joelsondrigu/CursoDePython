"""
print("SOFTWARE PINTOR")
nl = float(input('Digite a largura da parede: '))
na = float(input('Digite a altura da parede: '))
nm = nl * na
nqtdt = nm / 2
print('Sua parede tem {} m2 e vc precisa de {} litros de tinta para pinta-la'  .format(nm,nqtdt))

print("LIQUIDAÇÃO")
npreco = float(input('Insira o valor do produto: '))
ndesc = npreco * 5 /100
print('O valor do produto com desconto é: {}' .format(ndesc))

sal = float(input('Qual é o seu salário no atual momento? '))
aument = sal*15/100
salnovo = aument + sal
print(f'O seu salário atual é de R${sal}, com o aumento de 15% ficará R${salnovo}')
"""
print('SALÁRIOS SOF')
nsal = float(input('Digite seu salário: '))
nsau = nsal + (nsal*15/100)
print('VC ganhou amento e Seu novo salário é {:.2f}'.format(nsau))



