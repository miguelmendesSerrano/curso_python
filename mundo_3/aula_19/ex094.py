# Unindo dicionários e listas
dados = {}
cadastro = []
while True:
    dados['nome'] = str(input('Nome: ')).capitalize()
    dados['sexo'] = str(input('Sexo: [M/F]')).strip().upper()
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('ERRO! Por favor digite apenas M ou F.')).strip().upper()
    dados['idade'] = int(input('Idade: '))
    cadastro.append(dados.copy())
    resp = str(input('Quer continuar? [S/N]')).strip().upper()
    while resp not in 'SN':
        resp = str(input('ERRO! Por favor, digite apenas S ou N.')).strip().upper()
    if resp == 'N':
        break
print('=' * 40)
print(cadastro)
print('=' * 40)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
total = []
for i in range(0, len(cadastro)):
    total.append(cadastro[i]['idade'])
media = sum(total) / len(cadastro)
print(f"B) A média de idade é de {media:.1f} anos.")
print('C) As mulheres cadastradas foram: ', end='')
for s in range(0, len(cadastro)):
    if cadastro[s]['sexo'] == 'F':
        print(f'{cadastro[s]["nome"]}', end=' ')
print('\nD) A lista de pessoas que estão acima da média: ')
for p in range(0, len(cadastro)):
    if cadastro[p]['idade'] >= media:
        print(f'nome = {cadastro[p]["nome"]}; sexo = {cadastro[p]["sexo"]}; idade = {cadastro[p]["idade"]}')
