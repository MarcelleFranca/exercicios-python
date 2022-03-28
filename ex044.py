print('{:*^40}'.format(" FRENCH STORE'S "))
print('-=-' * 14)
pag = float(input("Bem-Vindo a French Store's; Agora que escolheu seus produtos, digite o total a pagar: "))
forma = int(input("""FORMAS DE PAGAMENTO:
[ 1 ] À vista no dinheiro/cheque.
[ 2 ] À vista no cartão.
[ 3 ] 2x bo cartão.
[ 4 ] 3x ou mais no cartão.
Digite o número da opção escolhida:  """))
if forma == 1:
    desc = pag - (pag * 10 / 100)
    print('A opção desejada garante 10% de desconto ao consumidor, o valor total de sua compra será de R${:.2f}.'.format(desc))
elif forma == 2:
    desc = pag - (pag * 5 / 100)
    print('A opção desejada garante 5% de desconto ao consumidor, o valor total de sua compra será de R${:.2f}.'.format(desc))
elif forma == 3:
    desc = pag / 2
    print('A opção desejada parcela em duas vezes sua compra, cade parcela no valor de R${:.2f}, totalizando R${:.2f}!'.format(desc, pag))
elif forma == 4:
    parc = int(input('Em quantas vezes quer parcelar? LEMBRE-SE QQUE DEVE SER DE 3 OU MAIS VEZES NESSA OPÇÃO! '))
    if parc <= 3:
        desc = pag + (pag * 20 / 100)
        p = desc / parc
        print('A opção desejada lhe dará juros de 20%, totalizando R${:.2f}, sendo parcelada em {}x no cartão totalizando R${:.2f} por parcela.'.format(desc, parc, p))
    else:
        print('Parcelas desejadas imposiveis de serem efetivadas, tente novamente.')
else:
    print('Opção invalida, por favor, reinicie o processo de pagamento.')
print(" OBRIGADA POR ESCOLHER NOSSA LOJA! VOLTE SEMPRE!  ")
