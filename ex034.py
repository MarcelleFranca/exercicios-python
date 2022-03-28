sal = float(input('Hora do aumento, digite seu salário atual: R$'))
if sal < 1250.00:
    novo = sal + ((sal * 15) / 100)
    print('O seu salário de R${:.2f} recebe um aumento de 15%.\nSeu salário atual é de R${:.2f}.'.format(sal, novo))
else:
    novo = sal + ((sal * 10) / 100)
    print('O seu salário de R${:.2f} recebe i, aimento de 10%.\nSeu salário atual é de R${:.2f}.'.format(sal, novo))
