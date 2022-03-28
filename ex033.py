n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite outro número inteiro qualquer: '))
n3 = int(input('Agora o ultimo número inteiro qualquer: '))
# Verificando quem é o menor número!
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3
# Verificando o maior número!
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n2 and n3>n1:
    maior = n3
print('O maior número é o {}, e o menor número é {}.'.format(maior, menor))
