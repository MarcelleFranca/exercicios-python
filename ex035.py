print('-=-' * 20)
print('BEM-VINDO AO SEU ANALISADOR DE TRIÂNGULOS V1.0')
print('-=-' * 20)
s1 = float(input('Digite o primeiro segmento: '))
s2 = float(input('Digite o segundo segmento: '))
s3 = float(input('Digite o terceiro e último segmento: '))
if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
    print('Os seguintes segmentos conseguem formar um triângulo!')
else:
    print('Os segmentos propostos são incapazes de formar um triângulo.')
