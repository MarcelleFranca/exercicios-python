sexo = str(input('Digite o seu sexo biologico [M/F]: ')).upper().strip() [0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe o seu sexo biologico [M/F]: ')).upper().strip() [0]
print('Certo, sexo biologico definido como {}; registro concluído!.'.format(sexo))
