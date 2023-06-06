# Analisando Triângulos v2.0
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:  '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos \033[32mFORMAM\033[m um triângulo')
    if r1 == r2 == r3:
        print('O triângulo é \033[34mEQUILÁTERO\033[m')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é \033[32mESCALENO\033[m')
    else:
        print('O triângulo é \033[33mISÓSCELES\033[m')
else:
    print('Os segmentos \033[31mNÃO FORMAM\033[m um triângulo')
