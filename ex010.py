real = float(input('Quanto reais você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode contrar US${:.2f}.'.format(real, dolar))
