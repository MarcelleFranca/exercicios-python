print('-=-' * 25)
print("""Esse é o seu avaliador de média.
Por favor, siga as intruções, insira suas notas corretamente.
Somente assim saberá se vai estar de ferias ou retido.""")
print('-=-' * 25)
n1 = float(input('Por favor, digite sua primeira nota: '))
n2 = float(input('Agora sua segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta e última nota: '))
media = (n1 + n2 + n3 + n4) / 4
print("""Quem tirou as médias: 
{:.1f} no 1° Bimestre
{:.1f} no 2° Bimestre
{:.1f} no 3° Bimestre
{:.1f} no 4° Bimestre
Tem como média fina {:.1f}.""".format(n1, n2, n3, n4, media))
if media < 5:
    print('Infelizmente você está retido, e irá REPETIR DE ANO!')
elif media >= 5 and media < 7:
    print('Você está de RECUPERAÇÃO, aproveite para estudar o maximo possivel!')
elif media >= 7:
    print('PARABÉNS, VOCÊ FOI APROVADO!')
