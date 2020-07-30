"""for c in range(1,10):
    print(c)
print('Fim')

c = 1
while c <= 10:
    print('Conte:',c)
    c += 1
print('Fim')"""

n = 1
par = 0
impa = 0
while n != 0:
    n = int(input('Escreva um numero: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impa += 1

print('VC digitou {} impa e {} par '.format(impa,par))
print(impa)
print(par)












