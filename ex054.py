from datetime import date
cont1 = 0
cont2 = 0
for n in range(1, 8):
    nasc = int(input('Digite o ano de nascimentoda pessoa {}: '.format(n)))
    idade = date.today().year - nasc
    if idade >= 18:
        cont1 += 1
    elif idade <= 18:
        cont2 += 1
print('Existem {} pessoa(s) no grupo dos maiores de idade. \nE {} pessoa(s) no grupo dos menores de idade.'.format(cont1, cont2))
