# Boletim com listas compostas
boletim = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    boletim.append([nome, [nota_1, nota_2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{" BOLETIM ":=^22}')
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')
print('=' * 22)
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opcao == 999:
        break
    if opcao <= len(boletim) - 1:
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}')
print(f'{"PROGRAMA FINALIZADO":^22}')
