# Catetos e Hipotenusa
from math import hypot
cat_op = float(input('Valor do cateto oposto: '))
cat_ad = float(input('Valor do cateto adjacente: '))
hip = hypot(cat_op, cat_ad)
print('O valor da hipotenusa é: {:.2f}'.format(hip))
