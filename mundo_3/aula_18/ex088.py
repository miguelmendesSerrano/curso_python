#  Palpites Mega Sena
from random import randint
from time import sleep
palpite = []
jogos = []
print('=' * 30)
print(f'{"JOGOS DA MEGA SENA":^30}')
print('=' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{" SORTEANDO... ":=^30}')
for j in range(0, quant):
    print(f'Jogo {j+1:2}: ', end='')
    for i in range(0, 6):
        valor = randint(0, 60)
        if valor not in palpite:
            palpite.append(valor)
        else:
            valor = randint(0, 60)
            palpite.append(valor)
        palpite.sort()
    print(palpite)
    jogos.append(palpite[:])
    palpite.clear()
    sleep(1)
print(f'{" BOA SORTE! ":=^30}')
