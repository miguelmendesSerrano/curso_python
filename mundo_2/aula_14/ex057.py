# Validação de Dados
nome = input('Nome: ')
sexo = input('Qual seu sexo[M/F]: ').strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = input('Valor inválido! Tente novamente.\nQual o seu sexo[M/F]: ').strip().upper()[0]
print('Dados resgistrado com sucesso.')
