print('-=-' * 25)
print('VEJAMOS COMO ANDA O SEU INDICE DE MASSA CORPORAL (IMC)!')
print('-=-' * 25)
sex = int(input("""Escolha uma das opções referente ao seu sexo biológico: 
[ 1 ] HOMEM
[ 2 ] MULHER
opção: """))
peso = float(input('Digite o seu peso: Kg '))
alt = float(input('Digite sua altura: M '))
imc = peso / (alt * alt)
#Opção do sexo masculino.
if sex == 1:
    print('Seu IMC é {:.1f}, e ele está '.format(imc), end='')
    if imc <= 20.9: #baixo do peso é menor ou igual 20
        print('ABAIXO DO IDEAL! Por favor cuide da sua saúde!')
    elif 21.0 <= imc <= 24.9: #peso ideal é entre 21 e 24
        print('NA FAIXA IDEAL! Continue manténdo sua saúde.')
    elif 25.0 <= imc <= 29.9: #obsidade leve é entre 25 e 29
        print('COM OBSIDADE LEVE! Tenha cuidado e modere!')
    elif 30.0 <= imc <= 39.9: #obsidade moderada é entre 30 e 39
        print('COMO OBSIDADE MODERADA! Procure ajuda para cuidar de sua saúde!')
    elif imc <= 40.0: #obsidade morbita é de 40 para cima
        print('COM OBSIDADE MORBITA, PROCURE AJUDE!')
elif sex == 2:
    print('Seu IMC é {:.1f}, e ele está '.format(imc), end='')
    if imc <= 19.9: #baixo do peso é igual ou menor que 19
        print('ABAIXO DO IDEAL! Por favor cuide da sua saúde!')
    elif 20.0 <= imc <= 23.9: #peso ideal é entre 20 a 23
        print('NA FAIXA IDEAL! Continue manténdo sua saúde.')
    elif 24.0 <= imc <= 28.9: #obsidade leve é entre 24 e 28
        print('COM OBSIDADE LEVE! Tenha cuidado e modere!')
    elif 29.0 <= imc <= 39.9: #obsidade moderada é entre 29 e 39
        print('COMO OBSIDADE MODERADA! Procure ajuda para cuidar de sua saúde!')
    elif imc <= 40.0: #obsidade morbita é de 40 para cima
        print('COM OBSIDADE MORBITA, PROCURE AJUDE!')
else:
    print('Essa opção não existe, por favor, reinicie o programa.')
