#from math import factorial
#n = int(input('Digite um número para calcular seu Fatorial: '))
#f = factorial(n)
#print('O Fatorial de {} é {}.'.format(n, f))

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1 
# para fazer uma multiplicação limpa deve se começar com 1, pois tudo multiplicado por 0 dá 0
# isso. obviamente não se aplica a soma ou subtração.

print('CALCULANDO FATORIAL DE {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='' )
    f *= c
    c -= 1
print('{}'.format(f))
