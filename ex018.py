import math
an = float(input('Digite um ângulo qualquer: '))
co = math.cos(math.radians(an))
se = math.sin(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo {:.2f} tem como seno {:.2f}, o coseno é {:.2f} e a tangente {:.2f}.'.format(an, se, co, tan))
 