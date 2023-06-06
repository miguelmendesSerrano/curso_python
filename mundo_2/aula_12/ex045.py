# GAME: Pedra, Papel e Tesoura
from random import randint
from time import sleep
# definindo jogadas
itens = ['PEDRA', 'PAPEL', 'TESOURA']
# obtendo jogadas do computador
comput = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
# obtendo jogada do jogador
jogador = int(input('Qual sua jogada? '))
# mostrando jogadas
print('\033[36mJO')
sleep(0.8)
print('KEN')
sleep(0.8)
print('PO!!!\033[m')
print('=' * 24)
print('Computador jogou \033[31m{}\033[m'.format(itens[comput]))
print('Você jogou \033[32m{}\033[m'.format(itens[jogador]))
print('=' * 24)
# verificando jogadas e mostrando vencedor
if comput == 0:
    if jogador == 0:
        print('\033[34mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU !\033[m')
    elif jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU !\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA\033[m')
elif comput == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU !\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mJOGADOR VENCEU !\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA\033[m')
elif comput == 2:
    if jogador == 0:
        print('\033[32mJOGADOR VENCEU !\033[m')
    elif jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU !\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE\033[m')
    else:
        print('\033[33mJOGADA INVÁLIDA\033[m')
