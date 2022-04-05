print('=' * 40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('=' * 40)
p1 = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))
d = p1 + (10 - 1) * raz
for c in range(p1, d + raz, raz):
    print(c, end=' → ')
print('ACABOU!')