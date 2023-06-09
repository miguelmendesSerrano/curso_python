# Jogo do Par ou Ímpar
from random import randint
print('~' * 26)
print(' VAMOS JOGAR PAR OU ÍMPAR')
print('~' * 26)
cont = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    opcao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    while opcao != 'P' and opcao != 'I':
        opcao = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]
    print(f'Você jogo {jogador} e o computador {computador}. Total= {soma} ', end='')
    print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            print(f'Você PERDEU!\nVocê conseguiu vencer {cont} vezes.')
            break
    elif opcao == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!\nVamos jogar novamente...')
            cont += 1
        else:
            print(f'Você PERDEU!\nVocê conseguiu vencer {cont} vezes.')
            break
print('=' * 30)
