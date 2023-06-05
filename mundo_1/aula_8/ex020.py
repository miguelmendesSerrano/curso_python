# Sorteando uma ordem na lista
from random import shuffle
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista_alunos = [a1, a2, a3, a4]
shuffle(lista_alunos)
print('A ordem de apresentação será:\n{}'.format(lista_alunos))
