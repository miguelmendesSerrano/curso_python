# Grupo da Maioridade
from datetime import date
ano_atual = date.today().year
maior_idade = 0
menor_idade = 0
for i in range(1, 8):
    ano_nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(i)))
    if ano_atual - ano_nasc >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print('\nAo todo temos \033[34m{}\033[m pessoas maiores de idade'
      '\nE temos \033[33m{}\033[m pessoas menores de idade.'.format(maior_idade, menor_idade))
