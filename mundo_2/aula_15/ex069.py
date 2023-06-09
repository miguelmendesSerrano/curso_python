# Análise de dados do grupo
cont_idade = cont_homem = cont_mulher = 0
print('=' * 20)
print('Cadastro de Pessoas')
print('=' * 20)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'\nO total de pessoas com mais de 18 anos é de: {cont_idade}')
print(f'Ao todo temos {cont_homem} homem(s) cadastrado(s).')
print(f'E temos {cont_mulher} mulher(es) com menos de 20 anos.')
