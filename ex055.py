lst = []
for n in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(n)))
    lst += [peso]
print('O maior peso foi: {:.1f}'.format(max(lst)))
print('O menor peso foi: {:.1f}'.format(min(lst)))
