# Pintando Parede
largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
print('Area da parede: {:.2f} m²'.format(area))
print('A quantidade de tinta necessária é: {:.2f} lts'.format(area/2))
