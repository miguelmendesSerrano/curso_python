# Seno, Cosseno e Tangente
from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print('Para o angulo {}° temos que:\nO seno: {:.2f}\nO cosseno: {:.2f}\nA tangente: {:.2f}'.format(angulo, sen, cos, tang))
