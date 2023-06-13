# Jogos de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou: {v}.')
    sleep(0.8)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"<RANKING JOGADORES>":=^30}')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.8)
