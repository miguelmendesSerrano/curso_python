# Cadastro de Jogador de Futebol
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {c + 1}º partida? ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print(f'{"< DADOS >":=^30}')
print(jogador, '\n', '=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'--> Na {i + 1}º partida fez {v} gols.')
print(f'No total ele marcou {jogador["total"]} gols.')
