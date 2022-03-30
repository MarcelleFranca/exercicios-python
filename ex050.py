pares = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o valor do {}º número inteiro: '.format(c)))
    if n % 2 == 0:
        pares += n
        cont += 1
print('Você digitou {} números pares, e a soma deles é igual há {}.'.format(cont, pares))
