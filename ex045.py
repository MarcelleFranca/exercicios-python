from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Decida uma das opções e digite seu número: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=-' * 20)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=-' * 20)
if computador == 0:
    if jogador == 0:
        print('DEU EMPATE!')
    elif jogador == 1:
        print('O JOGADOR GANHOU!')
    elif jogador == 2:
        print('O COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('O COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('DEU EMPATE!')
    elif jogador == 2:
        print('O JOGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('O JOGADOR GANHOU!')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('DEU EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
