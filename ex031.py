dis = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dis))
if dis <= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print('O preço da sua passagem será de R${:.2f}.'.format(preco))
