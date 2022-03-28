preco = float(input('Qual é o valor do produto que você deseja comprar? R$'))
desconto = preco - (preco*5/100)
print('O produto que valia R${:.2f} recebe o desconto de 5% e seu valou atual é de R${:.2f}.'.format(preco, desconto))
