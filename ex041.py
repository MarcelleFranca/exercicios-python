from datetime import date
print('-=-' * 25)
print('Bem-vindo ao classificador de atletas.')
print('-=-' * 25)
print("""A Confederação Nacional de Natação atribuiu a este programa a categoriazação
dos atletas por meio de suas idades.""")
i = int(input('Digite o seu ano de nascimento: '))
idade = date.today().year - i
print('O atleta nascido em {} tem {} de idade, sendo assim: '.format(i, idade))
if idade <= 9:
    print('Você está categorizado como atleta MIRIM!')
elif idade <= 14:
    print('Você está categorizado como atleta INFANTIL!')
elif idade <= 19:
    print('Você está categorizado como atleta JÚNIOR!')
elif idade <= 25:
    print('Você está categorizado como atleta SÊMIOR!')
else:
    print('Você está classificado como atleta MASTER!')
