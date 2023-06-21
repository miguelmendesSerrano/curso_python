# Aprimorando os Dicionários
lista_jogadores = []
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols.clear()
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {p + 1}° partida? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista_jogadores.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite somente S ou N.')
    if resp == 'N':
        break
print('=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('=' * 40)
for k, v in enumerate(lista_jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 stop)'))
    if busca == 999:
        break
    if busca >= len(lista_jogadores):
        print('ERRO! Código de jogador não existe.')
    else:
        print(f'Levantamento de jogador {lista_jogadores[busca]["nome"]}:')
        for i, g in enumerate(lista_jogadores[busca]["gols"]):
            print(f' No jogo {i + 1} fez {g} gols.')
    print('=' * 40)
print('<< VOLTE SEMPRE >>')
