# Jogo da Adivinhação v2.0
from random import randint
tentativa = 1
comput = randint(0, 10)
print('''\033[1:31mVamos Jogar ???\033[m...\n
Acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar qual foi ?\n''')
jogador = int(input('Qual é seu palpite? '))
while comput != jogador:
    if jogador < comput:
        jogador = int(input('Mais...Tente de novo: '))
        tentativa += 1
    else:
        jogador = int(input('Menos...Tente de novo: '))
        tentativa += 1
print('\033[1:32mAcertou!\033[m Parabéns você acertou com {} tentativas.'.format(tentativa))
