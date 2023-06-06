# Alistamento Militar
from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))
genero = int(input('''Qual seu sexo? (1)Masculino (2)Feminino\n'''))
if genero == 2:
    print('Você não precisa se alistar.')
else:
    if atual - nasc < 18:
        print('Você precisa se alistar daqui a {} anos'.format(18 - (atual - nasc)))
    elif atual - nasc == 18:
        print('Voce deve se alistar \033[31mimediatamente!\033[m')
    else:
        print('Seu alistamento passou do prazo. Você deveria ter se alistado a {} anos.'.format((atual - nasc) - 18))
