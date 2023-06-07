# Analisador completo
soma = 0
homem_idade_maior = 0
nome_homem_velho = 0
mulher_20 = 0
for i in range(1, 5):
    print('----{}° PESSOA----'.format(i))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    if i == 1 and sexo == 'M':
        homem_idade_maior = idade
        nome_homem_velho = nome
    if sexo == 'M' and idade > homem_idade_maior:
        homem_idade_maior = idade
        nome_homem_velho = nome
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
print('A média de idade do grupo é de {} anos'.format(soma/4))
print('O homem mais velho tem {} anos e se chama {}'.format(homem_idade_maior, nome_homem_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher_20))
