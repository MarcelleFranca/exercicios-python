print('{:^40}'.format('SUPER PROGRASSÃO ARITMÉTICA'))
print('=-' * 20)
p1 = int(input('Digite o primeiro termo: '))
raz = int(input('Razão: '))

termo = p1
count = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais

    while count <= total:
        print('{} → '.format(termo), end='')
        termo += raz
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
