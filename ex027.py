n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('O seu primeiro nome é {}.'.format(nome[0]))
print('E o seu último nome é {}.'.format(nome[len(nome)-1]))
