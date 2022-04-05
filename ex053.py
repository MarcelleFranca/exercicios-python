frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]
"""for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]"""
if junto == inverso:
        print('A frase "{}" de trás para frente fica "{}" o que a torna um PALÍNDROMO!'.format(junto, inverso))
else:
        print('A frase "{}" de trás para frente fica "{}" então ela NÃO É UM PALÍNDROMO!'.format(junto, inverso))
