print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=-' * 20)
p1 = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))

termo = p1
count = 1

while count <= 10:
    print('{} → '.format(termo), end='')
    termo += raz
    count += 1
print('FIM!')
