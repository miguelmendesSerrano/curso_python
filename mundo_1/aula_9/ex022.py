# Analisador de textos
nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
print('O seu nome tem: {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem: {} letras.'.format(len(nome.split()[0])))
