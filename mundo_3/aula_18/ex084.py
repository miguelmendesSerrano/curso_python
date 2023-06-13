# Lista composta e análise de dados
lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maior:.1f} kg da(s) pessoa(s) ', end='')
for pessoa in lista:
    if pessoa[1] == maior:
        print(f'{pessoa[0]} ', end='')
print()
print(f'O menor peso foi de {menor} kg da(s) pessoa(s) ', end='')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'{pessoa[0]} ', end='')
