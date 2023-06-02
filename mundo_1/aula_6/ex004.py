# Dissecando uma Variável
v = input('Digite qualquer coisa: ')
print('O tipo primitivo desse valor é:', type(v))
print('Só tem espaços?', v.isspace())
print('É um número?', v.isnumeric())
print('É alfabético?', v.isalpha())
print('Está em maiúscula?', v.isupper())
print('Está em minúscula?', v.islower())
print('Está capitalizada?', v.istitle())

