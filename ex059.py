from time import sleep

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
maior = 0
solicit = ''

while solicit != 5:
    solicit = int(input("""    [ 1 ] Soma
    [ 2 ] Multiplicação
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do Programa
    >>>>>> Qual opção deseja executar? """))

    if solicit == 1:
        print('A soma entre {} + {} é {}'.format(v1, v2,v1 + v2))

    elif solicit == 2:
        print('O resultado de {} X {} é {}'.format(v1, v2, v1 * v2))

    elif solicit == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior entre {} e {} é {}'.format(v1, v2, maior))

    elif solicit == 4:
        print('Informe os novos números... ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))

    elif solicit == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente')

    print('=-='*20)
    sleep(1)

print('FIM DO PROGRAMA! Volte sempre :)')
