somaidade = 0
mediaidade = 0
maioridadeM = 0
nomevelho = ''
totfem = 0
for p in range(1, 5):
    print('_'*4, "{}° pessoa:".format(p), '_'*4)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    gener = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and gener in 'Mm':
        maioridadeM = idade
        nomevelho = nome
    if gener in 'Mm' and idade > maioridadeM:
        maioridadeM = idade
        nomevelho = nome
    if gener in 'Ff' and idade < 20:
        totfem += 1 
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chamar {}.'.format(maioridadeM, nome))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totfem))
