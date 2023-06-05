# Jogo da Adivinhação v.1.0
from random import choice
from time import sleep
lst_num = [0, 1, 2, 3, 4, 5]
num_escolhido = choice(lst_num)
num_entrada = int(input('Escolha um número entre 0 e 5: '))
print('Processando...')
sleep(1.5)
if num_escolhido == num_entrada:
    print('ACERTOU!!!\nO numero que você escolheu foi: {}\nO número sorteado foi: {}\nVocê acertou.'.format(num_entrada, num_escolhido))
else:
    print('ERROU!!!\nO número que você escolheu foi: {}\nO número sorteado foi: {}\nQue pena tente novamente.'.format(num_entrada, num_escolhido))
