from datetime import date
print('-=-' * 25)
print("""Você jovem sabia que ao completar 18 anos deve cumprir com o alistamento militar?
No entanto, apenas aqueles de sexo masculino devem cumprir com esse dever para com o seu país.""")
print('-=-' * 25)
sex = input("""Responda de acordo;
[FEM] - para mulheres.
[MASC] - para homens. 
Digite o seu sexo biologico: """)
if sex == 'FEM':
    print('Você não precisa cumprir com esse dever, mas não deixe de honrar sua pátria!')
elif sex == 'MASC':
    atual = date.today().year
    nasc = int(input(""""Você como homem deve cumprir com o seu papel e servir o seu país.
    Digite seu ano de nascimento: """))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos no atual ano de {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('DEVE SE ALISTAR IMEDIAAMENTE!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você AINDA não tem 18 anos. Falta {} anos para o seu alistamento!'.format(saldo))
    elif idade > 18:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos!'.format(saldo))
else:
    print('A opção digitada não se encontra entre as sugeridas, por favor, tente novamente.')
