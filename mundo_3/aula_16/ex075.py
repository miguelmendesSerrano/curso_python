# Análise de dados em uma Tupla
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
valores = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vez(es)')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não apareceu nenhuma vez.')
print('Os valores pares digitados foram: ', end='')
for i in valores:
    if i % 2 == 0:
        print(i, end=', ')
