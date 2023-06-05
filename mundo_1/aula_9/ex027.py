# Primeiro e último nome de uma pessoa
nome = input('Digite seu nome completo: ').strip()
print('Seu primeiro nome é: {}\nSeu último nome é: {}'.format(nome.split()[0], nome.split()[-1]))
