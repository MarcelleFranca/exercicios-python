from random import randint
coomp = randint(0, 10)
count = 0

print('-=-' * 20)
print('Pensei em um número entre 0 e 10, você consegue adivinhar?')
print('-=-' * 20)
player = int(input('Em qual número você acha que eu pensei? '))

while player != coomp:
    count += 1
    if player < coomp:
        player = int(input('Eu pensei em algo maior... Tente de novo. '))
    elif player > coomp:
        player = int(input('Ainda não! Tente novamente, só que menos... '))

print('EXATO! Eu pensei no número {}, você precisou de {} tentativas.'.format(coomp, count))
print('Gostaria de jogar novamente?')
