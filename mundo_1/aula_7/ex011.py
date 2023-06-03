# Pintando Parede
largura = float(input('Qual a largura da parede(em metros): '))
altura = float(input('Qual a altura da parede(em metros): '))
area = largura * altura
print('Area da parede: {:.2f} m²'.format(area))
print('A quantidade de tinta necessária é: {:.2f} l'.format(area/2))
