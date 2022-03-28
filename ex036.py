print('-=-' * 25)
print('BEM-VINDO AO SEU EMPRÉSTIMO, PARA INICIAR SIGA AS INTRUÇÕES ABAIXO!')
print('-=-' * 25)
salario = float(input('Qual é o seu salario atual? R$'))
casa = float(input('Qual é o valo do imóvel que pretende compar? R$'))
anos = int(input('Em quantos anos pretende financiar a casa? '))
fina = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para para um imóvel de R${:.2f} em {} ano(s), a prestação e será de R${:.2f}.'.format(casa, anos, fina))
if fina <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
