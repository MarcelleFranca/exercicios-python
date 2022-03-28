salario = float(input('Qual é o salário do funcionário? R$'))
salanovo = salario + (salario*15/100)
print('Um funcionario que recebia R${:.2f}, com o aumento de 15% passa a receber R${:.2f}.'.format(salario, salanovo))
