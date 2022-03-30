mult = int(input('Digite um número para saber sua tabuada: '))
print('-'*12)
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(mult, c, mult*c))
print('-'*12)
print('E essa é a tabuada do {}!'.format(mult))
