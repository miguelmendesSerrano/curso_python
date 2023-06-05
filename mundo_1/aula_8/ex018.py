# Seno, Cosseno e Tangente
from math import sin, cos, tan

angulo = float(input('Digite o angulo: '))
sen = sin(angulo)
cos = cos(angulo)
tang = tan(angulo)
print('Para o angulo {}° temos que:\nO seno: {:.2f}\nO cosseno: {:.2f}\nA tangente: {:.2f}'.format(angulo, sen, cos, tang))
