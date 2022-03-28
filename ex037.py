from time import sleep

print('-=-' * 25)
print('BEM-VINDO AO SEU CONVERSOR DE BASES NÚMERICAS!')
print('-=-' * 25)
sleep(2)
inteiro = int(input('Digite um número inteiro: '))
print('Escolhas uma das bases númericas para conversão')
sleep(3)
print('[ 1 ] converter para BINÁRIO')
sleep(3)
print('[ 2 ] converter para OCTAL')
sleep(3)
print('[ 3 ] converter para HEXADECIMAL')
num = int(input('Sua opção é: '))
if num == 1:
    print('Opção desejada para conversão, BINÁRIO!')
    print('O número inteiro {} convertido para Binário é {}.'.format(inteiro, bin(inteiro) [2:] ))
elif num == 2:
    print('Opção desejada para conversão, OCTAL!')
    print('O número inteiro {} convertido para Octal é {}.'.format(inteiro, oct(inteiro) [2:] ))
elif num == 3:
    print('Opção desejada para conversão, HEXADECIMAL!')
    print('O número inteiro {} convertido para Hexadecimal é {}.'.format(inteiro, hex(inteiro) [2:] ))
else:
    print('Esse número não remete as opções propostas, por favor, reinicie o conversor!')
