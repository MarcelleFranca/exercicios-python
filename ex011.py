lar = float(input('Qual é a largura da parede: '))
alt = float(input('E qual é a altura da parede: '))
area = lar * alt
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(lar, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.1f}l de tinta.'.format(tinta))
