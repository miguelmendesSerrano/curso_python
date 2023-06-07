# Maior e menor da sequencia
lista_pesos = []
for i in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(i)))
    lista_pesos += [peso]
print('O maior peso da lista é: {} kg'.format(max(lista_pesos)))
print('O menor peso da lista é: {} kg'.format(min(lista_pesos)))
