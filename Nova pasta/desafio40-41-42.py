"""
n1 = float(input('Entre com a primeira nota do aluno: '))
n2 = float(input('Entre com a segunda nota do aluno: '))
media = (n1+n2)/2
if media >= 7:
    print('PARABÉNS! VC FOI APROVADO COM {:.2f}'.format(media))
elif media > 5 and media < 6.9:
   print('sua média foi {:.2f} e VC FICOU DE RECUPERAÇÃO! continue os estudos!'.format(media))
elif media < 5:
    print('SUA MÉDIA FOI {:.2f} E VC FOI REPROVADO! MAS NÃO DESISTA!'.format(media))
"""
from datetime import date
ano = date.today().year
print('==========CN NATAÇÃO==========')
print('----------CATEGORIAS----------')
ano_nasc = int(input('DIGITE O ANO DE SEU NASCIMENTO: '))
idade = ano - ano_nasc
if idade <= 9:
    print('vc tem {} anos e é atleta pertecente a categoria MIRIM'.format(idade))
elif idade <= 14:
    print('vc tem {} anos e é atleta pertecente a categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('vc tem {} anos e é atleta pertecente a categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('vc tem {} anos e é atleta pertecente a categoria PROFISSIONAL'.format(idade))
elif idade > 25 and idade < 50:
    print('vc tem {} anos e é atleta pertecente a categoria MASTER'.format(idade))
else:
    print('[ERRO] revise os dados e tente novamente!')