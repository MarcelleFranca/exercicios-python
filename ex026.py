frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na sua frase.'.format(frase.count('A')))
print('A primeira vez que a letra A aparece, é na posição {}.'.format(frase.find('A')+1))
print('A ultima vez que a letra A aparece é na posição {}.'.format(frase.rfind('A')+1))
