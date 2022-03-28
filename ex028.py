from random import randint
coomp = randint(0, 5)
print('-=-' * 20)
print('Pensei em um número entre 0 e 5, você consegue adivinhar?')
print('-=-' * 20)
player = int(input('Em qual número você acha que eu pensei? '))
if coomp == player:
    print('VOCÊ GANHOU! Eu pensei no número {}.'.format(coomp))
else:
    print('Infelizmente você perdeu, o número que eu pensei foi {}.'.format(coomp))
print('Gostaria de jogar novamente? De play!')
