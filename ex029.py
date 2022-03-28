v = float(input('Qual é a velocidade do carro? Km/h:'))
if v > 80:
    print('MULTADO! Você excedeu o limitede de velocidade permitido, que é 80km/h.')
    multa = (v-80) * 7
    print('O valor da multa a paga é R${:.2f}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
