num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('E esse é um número PRIMO!')
else:
    print('E por isso ele NÃO é um número primo.')
