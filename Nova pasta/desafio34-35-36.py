"""
salario = float(input('DIGITE SEU ATUAL SALÁRIO: '))
if salario > 3000:
    aumento = salario + (salario * 10 / 100)
    print('PARABÉNS! VC GANHOU AUMENTO DE 10%''. Seu novo salário é de: R$ {:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 15 /100)
    print('PARABÉNS! VC GANHOU AUMENTO DE 15%''. Seu novo salário é de: R$ {:.2f}'.format(aumento))
"""
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o salario do comprador: R$ '))
tempo = int(input('Digite o tempo de financiamento: '))
meses = tempo * 12
parcela = casa / meses
maximo = salario * 30/100
if parcela <= maximo:
    print('PARABÉNS! VC TEVE SEU FINANCIAMENTO APROVADO!')
    print('Segue as condições: ')
    print('O valor da parcela será de: R$ {:.2f} em: {} meses. somando um total de: R$ {:.2f} Reais '.format(parcela,meses,casa))
else:
    print('A VALOR DA PARCELA FICOU ACIMA DA MÁXIMA PERMITIDA PARA SEU SCORE')




