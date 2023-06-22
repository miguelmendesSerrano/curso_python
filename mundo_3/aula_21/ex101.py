# Funções para votação
from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade <= 15:
        print(f'Com {idade} anos: NÂO VOTA')
    elif 17 > idade >= 16:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    elif 65 > idade >= 18:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL')


ano = int(input('Em que ano você nasceu? '))
voto(ano)

