m = float(input('Digite qualquer valor em metros e iremos convertelo: '))
#Lembresse que METROS equivale a 1, antes dele vem dm, cm e mm; para cada um desses acrescente 0 após o 1
#para saber km, hm e dam, acreste 0 antes do 1
print('Convertendo o valor para milímetro fica {}.'.format(m*1000))
print('Em centímetro fica {}.'.format(m*100))
print('Em decímetro fica {}.'.format(m*10))
print('Agora em decâmetro fica {:.1f}.'.format(m/10))
print('Em hectômetro é {:.2f}.'.format(m/100))
print('Em quilômetro ficaria {:.3f}.'.format(m/1000))
